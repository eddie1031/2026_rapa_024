from fastapi import FastAPI
from app.boards.router import router as board_router

import app.boards.models
import app.posts.models

app = FastAPI()

app.include_router(router=board_router)



