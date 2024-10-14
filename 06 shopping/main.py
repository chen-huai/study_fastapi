from typing import Union

from fastapi import FastAPI

import uvicorn

from app01.urls import user

from app02.urls import shop

app = FastAPI()

app.include_router(shop, prefix="/shop",tags=["购物中心接口"])

app.include_router(user, prefix="/user",tags=["用户中心接口"])

if __name__ == '__main__':

    uvicorn.run("main:app", port=8080, reload=True)