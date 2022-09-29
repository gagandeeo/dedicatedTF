from typing import Union
from test_model import prepare_image, load_model, predict
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
# import download_model

app = FastAPI()

# download_model.download_model()
model = load_model("./mobilenetV2")

origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers    
)

@app.get("/hello")
def hello_world():
    return {"result": "helloworld"}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    content = await file.read()
    preprocess_img = prepare_image(content)
    res = predict(preprocess_img, model)
    res = res[0][:,1:]
    return {"result": res}

# if __name == "__main__":
#     run(app, host="0.0.0.0", port=5000)
