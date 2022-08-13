from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
import uvicorn

from db.base import database
from endpoints import users, auth, apartments, buildings, reviews
from html import html
from manager import manager


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


@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    await manager.broadcast(f"Client #{client_id} join the chat")
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='localhost', reload=True)
