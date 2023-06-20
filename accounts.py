import json
from fastapi import FastAPI

app = FastAPI()

USERS_FILE = "users.json"

def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def write_json_file(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

@app.post("/login")
def login(username: str, password: str):
    users = read_json_file(USERS_FILE)
    for user in users:
        if user["username"] == username and user["password"] == password:
            token = generate_token(username)
            return {"token": token}
    return {"message": "Invalid username or password"}

@app.post("/signup")
def signup(username: str, password: str):
    users = read_json_file(USERS_FILE)
    for user in users:
        if user["username"] == username:
            return {"message": "Username already exists"}
    new_user = {"username": username, "password": password}
    users.append(new_user)
    write_json_file(USERS_FILE, users)
    return {"message": "Account created successfully"}

@app.delete("/logout")
def logout(token: str):
    # Your logic to delete the token and log the user out
    return {"message": "Logged out successfully"}

@app.get("/check_token")
def check_token(token: str):
    # Your logic to validate the token and retrieve user information
    return {"user": None}

