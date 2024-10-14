
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/get")
def get_test():
    return {"method":"get方法"}

@app.post("/post",
        tags=["这是test的post功能"],
        description='这个功能的详情信息',
        response_description='这个是相应后的信息',
          )
def post_test():
    return {"method":"post方法"}

@app.put("/put")
def put_test():
    return {"method":"put方法"}

@app.delete("/delete")
def delete_test():
    return {"method": "delete?"}

if __name__ == '__main__':
    uvicorn.run("04 路径操作参数:app", port=8081, log_level=True, reload=True)