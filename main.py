from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("index.html")

@app.get("/{item_name}")
def page(item_name: str):
    path = item_name
    return FileResponse(path)

@app.get("/{root_src}/{item_name}")
def source(root_src: str, item_name: str):
    path = root_src + "/" + item_name
    return FileResponse(path)