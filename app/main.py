from fastapi import FastAPI
from app.routers.wm import router as router_wm


app = FastAPI()

app.include_router(router_wm)