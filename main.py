
from fastapi import FastAPI, APIRouter

app = FastAPI()

app.title = 'Api Pelicula'
app.version = '2'

decorator = APIRouter
@app.get('/')
async def endpointPrueba():
    return 'HOLA MUNDO'