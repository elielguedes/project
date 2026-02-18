from fastapi import FastAPI
from app.routers.user import router
from app.routers.records import RouterRecords
from app.routers.crime import RouterCrime

app = FastAPI()

app.include_router(router)
app.include_router(RouterRecords)
app.include_router(RouterCrime)
