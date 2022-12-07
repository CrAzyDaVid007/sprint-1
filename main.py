from fastapi import FastAPI

app = FastAPI()

@app.get("/saludo")
async def root():
    return {"message": "Hola MisionTIC 2022"}

@app.get("/usuarios/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}

autos = [{"auto": "subaru impreza sti"}, 
         {"auto": "toyota supra"},
         {"auto":"audi r8"} ,
         {"auto": "lincon navigator"}]

@app.get("/autos/")
async def read_item(skip: int = 0, limit: int = 10):
    return autos[skip : skip + limit]