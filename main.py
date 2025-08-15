from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


  async def funcaoteste():
    return {"teste": True, "um_aleatorio": random.randint(0,20000)}