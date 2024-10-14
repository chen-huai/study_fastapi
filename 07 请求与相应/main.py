from typing import Union

from fastapi import FastAPI

import uvicorn

from apps.app01 import app01

app = FastAPI()

app.include_router(app01, tags=["01 路径参数"])

# app.include_router(user, prefix="/user",tags=["用户中心接口"])

if __name__ == '__main__':

    uvicorn.run("main:app", port=8080, reload=True)