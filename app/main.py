from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {
        "message": "백엔드 화이팅!"
    }

