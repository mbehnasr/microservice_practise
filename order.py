
from fastapi import FastAPI
import json

app = FastAPI()

orders_file = "orders.json"

def load_orders():
    try:
        with open(orders_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_orders(orders):
    with open(orders_file, "w") as file:
        json.dump(orders, file)

@app.on_event("startup")
def startup_event():
    global orders
    orders = load_orders()

@app.post("/add_order")
def add_order(order_id: str):
    # Add the order to the list of orders
    # ...
    save_orders(orders)
    return {"message": "Order added successfully"}

@app.get("/get_orders")
def get_orders():
    return {"orders": orders}

@app.get("/get_order_detail")
def get_order_detail(order_id: str):
    # Retrieve the order details
    # ...
    return {"order": order}

