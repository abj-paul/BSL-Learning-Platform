from fastapi import FastAPI;
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

@app.post("/registration")
def register_new_user(user:str):
    user = unquote(user)
    print(user)
    user = User(user.username, user.password, user.institution_name, user.email, user.role)
    add_user(user)
    authToken = createSession(user)
    return {"Status":"Success", "authToken": authToken }

@app.post("/login")
def authenticate(username: str, password: str):
    user = checkIfCredentialsAreCorrect(username, password)
    if user==None: return {"Status": WRONG_CREDENTIALS }
    authToken = createSession(user)
    return {"Status": "Success", "authToken": authToken, "role":user.role}

@app.get("/logout")
def logout(authToken:str, role:str):
    if authorize(authToken, role) == False: return {"Status": UNAUTHORIZED_ACCESS}
    deleteSession(authToken, role)
    return {"Status": "Success"}

@app.get("/student_dashboard")
def send_student_dashboard_contents(authToken:str, role:str):
    if role.upper() != "STUDENT": return {"Status": WRONG_USER_UNAUTHORIZED_ACCESS}
    if authorize(authToken, role) == False: return {"Status": UNAUTHORIZED_ACCESS}
    return {"Yay": "Yayy"}

@app.get("/registration")
def get_user_list(authToken:str, role:str):
    if authorize(authToken, role) == False: return {"Status": UNAUTHORIZED_ACCESS}
    return get_registered_users()