from fastapi import FastAPI, Request;
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import unquote

from User import User;
from temp_db import *;

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root(test, test2):
    return [test, test2]

@app.post("/registration/")
async def register_new_user(request: Request):
    userdata = await request.json()
    print(userdata)


    user = User(userdata["username"], userdata["password"], userdata["institution"], userdata["email"], userdata["role"])
    add_user(user)
    authToken = createSession(user)
    return {"Status":"Success", "authToken": authToken,"role":user.role }



@app.post("/login/")
async def authenticate(request: Request):
    userdata = await request.json()

    user = checkIfCredentialsAreCorrect(userdata["username"], userdata["password"])
    if user==None: return {"Status": WRONG_CREDENTIALS }
    authToken = createSession(user)
    return {"Status": "Success", "authToken": authToken, "role":user.role}

@app.post("/logout/")
async def logout_user(request: Request):
    userdata = await request.json()

    if authorize(userdata["authToken"], userdata["role"]) == False: return {"Status": UNAUTHORIZED_ACCESS}
    deleteSession(userdata["authToken"], userdata["role"])
    return {"Status": "Success"}

@app.get("/student_dashboard/profile/")
def send_student_dashboard_profile(authToken:str, role:str):
    if role.upper() != "STUDENT": return {"Status": WRONG_USER_UNAUTHORIZED_ACCESS}
    if authorize(authToken, role) == False: return {"Status": UNAUTHORIZED_ACCESS}

    user = getUserData(authToken, role)
    return {"Status":"Success", "username": user.username, "insitution":user.institution_name, "email":user.email, "role":user.role}

@app.get("/teacher_dashboard/profile/")
def send_teacher_dashboard_profile(authToken:str, role:str):
    if role.upper() != "TEACHER": return {"Status": WRONG_USER_UNAUTHORIZED_ACCESS}
    if authorize(authToken, role) == False: return {"Status": UNAUTHORIZED_ACCESS}

    user = getUserData(authToken, role)
    return {"Status":"Success", "username": user.username, "insitution":user.institution_name, "email":user.email, "role":user.role}

@app.get("/registration")
def get_user_list(authToken:str, role:str):
    if authorize(authToken, role) == False: return {"Status": UNAUTHORIZED_ACCESS}
    return get_registered_users()