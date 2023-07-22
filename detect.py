import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import torch
import os


app = FastAPI()

# CORSミドルウェアを追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 全てのオリジンからのアクセスを許可
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get-images")
async def getImages():
    print("get-images")

    folder_path = "images"  # フォルダのパスを指定

    file_names = []

    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            file_names.append(file_name)

    print("get-images2")
    return file_names


@app.get("/detect")
async def detect(data: str):
    # Model
    model = torch.hub.load(
        "ultralytics/yolov5", "yolov5s"
    )  # or yolov5n - yolov5x6, custom

    # Images
    img = "images/" + data  # or file, Path, PIL, OpenCV, numpy, list

    # Inference
    results = model(img)

    # Results
    results.print()  # or .show(), .save(), .crop(), .pandas(), etc.

    results.show()
    results.save()

    return {"message": "Hello detect"}


# オプション(host=0.0.0.0とし、EC2の外部IPアドレスを指定してアクセス可能にする)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
