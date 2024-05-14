import databases

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from app.core import settings
from app import routers

db = databases.Database(settings.POSTGRES_URL)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()

app = FastAPI(lifespan=lifespan)
add_pagination(app)

app.include_router(routers.realty_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def status_check():
    return {"status": settings.POSTGRES_URL}
