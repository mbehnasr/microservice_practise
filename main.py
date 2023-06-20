from fastapi import FastAPI
from fastapi.routing import APIRouter
from accounts import accounts_app
from shop import shop_app
from order import order_app

app = FastAPI()

router = APIRouter()
router.include_router(accounts_app, prefix="/accounts", tags=["Accounts"])
router.include_router(shop_app, prefix="/shop", tags=["Shop"])
router.include_router(order_app, prefix="/order", tags=["Order"])

app.include_router(router)

