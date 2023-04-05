from fastapi import FastAPI, Request;
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import unquote

from User import User
from AuthServices import *
from constants import *
from Mail import *
from Model import *

drop_table()
create_user_table()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def root():
    return "Hello World!"


@app.post("/register/")
async def register_user(request: Request):
    userdata = await request.json()
    print("register/:" +str(userdata))

    user = User(userdata["username"], userdata["password"], userdata["institution"], userdata["email"], userdata["role"])
    otp = createOTPForUser(user)
    print("#####Generated OTP: "+str(otp)) # mail OTP
    send_mail("Please enter the following OTP in BSL Learning Platform to confirm your account! "+str(otp), user.email)
    return {"Status":"Registration Success", "Next Operation":"Verify OTP to confirm your account.", "OTP":otp }

@app.post("/register/OTP/")
async def verify_otp(request: Request):
    userdata = await request.json()
    print("register/OTP/:" +str(userdata))

    user = User(userdata["username"], userdata["password"], userdata["institution"], userdata["email"], userdata["role"])
    if validateOTP(user, userdata["OTP"]) == False: 
        return WRONG_OTP
    
    add_user(user)
    authToken = createSession(user)
    return {"Status":"OTP Success", "authToken": authToken }

@app.post("/login/")
async def login_user(request: Request):
    userdata = await request.json()
    print("login/:" +str(userdata))

    checkVal = checkIfUserExists(userdata["username"], userdata["password"])
    if checkVal == False:
        return WRONG_LOGIN_CREDENTIALS
    userdata = checkVal
    user = User(userdata[1], userdata[2], userdata[3], userdata[4], userdata[5])

    authToken = createSession(user)
    return {"Status":"Login Success", "authToken": authToken, "username": user.username, "email": user.email, "institution": user.institution, "role": user.role}

@app.post("/login/forgot_password/")
async def user_forgot_password(request: Request):
    userdata = await request.json()
    print("/login/forgot_password/:" +str(userdata))

    OTP = forget_password(userdata["email"])

    return {"Status":"Forget Password OTP Success", "OTP": OTP }

@app.post("/login/forgot_password/OTP")
async def user_forgot_password(request: Request):
    userdata = await request.json()
    print("/login/forgot_password/:" +str(userdata))

    if update_password(userdata["email"], userdata["OTP"], userdata["new_password"]) == False: return FORGOT_PASSWORD_OPERATION_FAILED

    return {"Status":"Forget Password Success", "Next Action": "Please Login now." }

@app.post("/logout/")
async def user_logout_controller(request: Request):
    userdata = await request.json()
    print("/logout/:" +str(userdata))

    deleteSession(userdata["authToken"])
    return {"Status":"Logout Successful" }
