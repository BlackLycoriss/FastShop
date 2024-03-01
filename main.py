from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("index.html")

@app.get("/index.html")
def index_page():
    return FileResponse("index.html")

@app.get("/about.html")
def about_page():
    return FileResponse("about.html")

@app.get("/contacts.html")
def contacts_page():
    return FileResponse("contacts.html")

@app.get("/catalog.html")
def catalog_page():
    return FileResponse("catalog.html")