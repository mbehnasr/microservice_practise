
from fastapi import FastAPI
import json

app = FastAPI()

items_file = "items.json"
cart_file = "cart.json"

def load_items():
    try:
        with open(items_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_items(items):
    with open(items_file, "w") as file:
        json.dump(items, file)

def load_cart():
    try:
        with open(cart_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_cart(cart):
    with open(cart_file, "w") as file:
        json.dump(cart, file)

@app.on_event("startup")
def startup_event():
    global items, cart
    items = load_items()
    cart = load_cart()

@app.post("/add_to_cart")
def add_to_cart(item_id: str, token: str):
    if token in users:
        cart.append({"item_id": item_id, "user": users[token]["username"]})
        save_cart(cart)
        return {"message": "Item added to cart"}
    return {"message": "Invalid token"}

@app.get("/get_items")
def get_items():
    return {"items": items}

@app.get("/item_detail")
def item_detail(item_id: str):
    if item_id in items:
        return {"item": items[item_id]}
    return {"message": "Item not found"}

@app.delete("/remove_from_cart")
def remove_from_cart(item_id: str, token: str):
    if token in users:
        for item in cart:
            if item["item_id"] == item_id and item["user"] == users[token]["username"]:
                cart.remove(item)
                save_cart(cart)
                return {"message": "Item removed from cart"}
        return {"message": "Item not found in cart"}
    return {"message": "Invalid token"}

@app.post("/add_order")
def add_order(token: str):
    if token in users:
        order_id = generate_order_id()
        # Finalize the cart and process the order
        # ...
        return {"order_id": order_id}
    return {"message": "Invalid token"}

@app.post("/pay_order")
def pay_order(order_id: str):
    # Process the payment for the order
    # ...
    return {"message": "Payment successful"}

