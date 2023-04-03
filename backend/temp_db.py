import datetime 

registered_users = []
running_sessions = []

UNAUTHORIZED_ACCESS = "UNAUTHORIZED_ACCESS"
WRONG_CREDENTIALS = "WRONG_CREDENTIALS"
WRONG_USER_UNAUTHORIZED_ACCESS = "WRONG_USER_UNAUTHORIZED_ACCESS"

def add_user(user):
    registered_users.append(user)

def get_registered_users():
    return registered_users

def checkIfCredentialsAreCorrect(username, password):
    print(registered_users)
    for user in registered_users:
        if user.username == username and user.password == password:
            return user 
    return None

def createSession(user):
    session = []
    session.append(user.role)
    authToken = str(hash(str(user)+str(datetime.datetime.now())))
    session.append(authToken)
    session.append(user)

    running_sessions.append(session)

    return authToken

def deleteSession(authToken, role):
    for session in running_sessions:
        if session[0]==role and session[1]==authToken: running_sessions.remove(session)

def getUserData(authToken, role):
    for session in running_sessions:
        if session[0]==role and session[1]==authToken: return session[2]
    return None


def authorize(authToken, role):
    print(running_sessions, authToken, role)
    for session in running_sessions:
        if session[0]==role and session[1]==authToken: return True 
        print("session[1]==authToken:"+str(session[1]==authToken))
    return False 