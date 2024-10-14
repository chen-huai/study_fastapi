from fastapi import APIRouter

app01 = APIRouter()

@app01.get('/app01/{id}')
def app01_get(id: int):
    return {
        'id':id
    }