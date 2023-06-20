
from fastapi import FastAPI
import json

app = FastAPI()

users_file = "accounts.json"

def load_users():
    try:
        with open(users_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(users_file, "w") as file:
        json.dump(users, file)

@app.on_event("startup")
def startup_event():
    global users
    users = load_users()

@app.post("/login")
def login(username: str, password: str):
    if username in users and users[username]["password"] == password:
        token = generate_token()
        users[username]["token"] = token
        save_users(users)
        return {"token": token}
    return {"message": "Invalid credentials"}

@app.post("/signup")
def signup(username: str, password: str):
    if username in users:
        return {"message": "Username already exists"}
    token = generate_token()
    users[username] = {"password": password, "token": token}
    save_users(users)
    return {"message": "User registered successfully"}

@app.post("/logout")
def logout(username: str):
    if username in users:
        users[username]["token"] = ""
        save_users(users)
        return {"message": "Logout successful"}
    return {"message": "Invalid username"}

@app.get("/check_token")
def check_token(token: str):
    for username, user_info in users.items():
        if user_info["token"] == token:
            return {"user": username}
    return {"message": "Invalid token"}

