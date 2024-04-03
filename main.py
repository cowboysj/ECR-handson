from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hellofff, World!"}

@app.get("/test")
async def root():
    return "Hello, test page!!"

@app.get("/test2")
async def root():
    return "test2"