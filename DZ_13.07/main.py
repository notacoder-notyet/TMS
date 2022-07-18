from fastapi import FastAPI
import uvicorn

from db.base import database
from endpoints import users, auth, apartments, buildings, reviews

app = FastAPI(title='Rent apartments')
app.include_router(users.router, prefix='/users', tags=['users'])
app.include_router(auth.router, prefix='/auth', tags=['auth'])
app.include_router(apartments.router, prefix='/apartments', tags=['apartments'])
app.include_router(buildings.router, prefix='/buildings', tags=['buildings'])
app.include_router(reviews.router, prefix='/reviews', tags=['reviews'])

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, host='localhost', reload=True)