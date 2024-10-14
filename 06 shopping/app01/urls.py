# from fastapi import FastAPI
from fastapi import APIRouter

user = APIRouter()

@user.post ("/login")
def user_login():

    return {"user": "Login"}

@user.post ("/rel")
def user_reg():

    return {"user": "reg"}