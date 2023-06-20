import json
from fastapi import FastAPI

app = FastAPI()

# File paths
USERS_FILE = "users.json"
CARTS_FILE = "carts.json"
ITEMS_FILE = "items.json"
ORDERS_FILE = "orders.json"

# Helper functions for reading and writing JSON data

def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def write_json_file(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


# Accounts Service

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


# Shop Service

@app.post("/add_to_cart")
def add_to_cart(item_id: str, token: str):
    # Your logic to add an item to the user's cart
    return {"message": "Item added to cart successfully"}

@app.get("/get_items")
def get_items():
    # Your logic to retrieve all available items
    return {"items": []}

@app.get("/item_detail")
def item_detail(item_id: str):
    # Your logic to retrieve detailed information about an item
    return {"item": None}

@app.post("/remove_from_cart")
def remove_from_cart(item_id: str, token: str):
    # Your logic to remove an item from the user's cart
    return {"message": "Item removed from cart successfully"}

@app.post("/add_order")
def add_order(token: str):
    # Your logic to finalize the cart and create an order
    return {"order_id": None}

@app.post("/pay_order")
def pay_order(order_id: str):
    # Your logic to process the payment for an order
    return {"message": "Payment successful"}


# Order Service

@app.get("/get_orders")
def get_orders():
    # Your logic to retrieve all orders
    return {"orders": []}

@app.get("/get_order_detail")
def get_order_detail(order_id: str):
    # Your logic to retrieve detailed information about an order
    return {"order": None}

