import asyncio
import datetime
import httpx

from fastapi import FastAPI
from . import db

URL = 'http://worldclockapi.com/api/json/est/now'


def get_app():
    app = FastAPI()
    db.db.init_app(app)
    return app


app = get_app()


async def fetch_snapshot(url):
    while True:
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{url}")
            snapshot = resp.text
            date = datetime.datetime.now()
            await db.Snapshots.create(timestamp=date, snapshot=snapshot)
            await asyncio.sleep(30)


@app.get('/')
async def root():
    message = 'Last 5 logs from database:'
    last_logs = await db.Snapshots.query.order_by(
        db.Snapshots.timestamp.desc()).limit(5).gino.all()
    return message, last_logs


@app.on_event('startup')
def startup_event():
    asyncio.create_task(fetch_snapshot(url=URL))
