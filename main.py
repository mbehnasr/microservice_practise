
from fastapi import FastAPI
from accounts import app as accounts_app
from shop import app as shop_app
from order import app as order_app

app = FastAPI()

app.mount("/accounts", accounts_app)
app.mount("/shop", shop_app)
app.mount("/order", order_app)

