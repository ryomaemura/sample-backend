import uvicorn  # uvicornのインポートを追加
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# オプション(host=0.0.0.0とし、EC2の外部IPアドレスを指定してアクセス可能にする)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
