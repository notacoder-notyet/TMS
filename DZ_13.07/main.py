from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn

from db.base import database
from endpoints import users, auth, apartments, buildings, reviews
from html import html


app = FastAPI(title='Rent apartments')

app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(apartments.router, prefix='/apartments', tags=['apartments'])
app.include_router(buildings.router, prefix='/buildings', tags=['buildings'])
app.include_router(reviews.router, prefix='/reviews', tags=['reviews'])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='localhost', reload=True)
