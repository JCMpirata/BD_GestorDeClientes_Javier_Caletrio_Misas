from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr, validator
import database as db
import helpers as hlp


headers = {"content-type": "charset=utf-8"}


class Modelo_de_Cliente(BaseModel):
    id: int
    nombre: constr(min_length=3, max_length=50)
    apellido: constr(min_length=3, max_length=50)
    dni: constr(min_length=8, max_length=8)

    @validator("id")
    def id_valido(cls, v):
        if not hlp.validar_id(v, db.clientes):
            raise ValueError("ID no válido")
        return v

    @validator("dni")
    def dni_valido(cls, v):
        if not hlp.validar_dni(v):
            raise ValueError("DNI no válido")
        return v
    

app = FastAPI(title="API de clientes", description="API para gestionar clientes", version="1.0.0")


@app.get("/clientes", tags = ["Clientes"])
async def listar_clientes():
    content = [db.Cliente.to_dict(cliente) for cliente in db.Clientes.lista]
    return JSONResponse(content=content, headers=headers)


@app.get("/clientes/{id}", tags = ["Clientes"])
async def buscar_cliente(id: int):
    cliente = db.Clientes.buscar(id)
    if cliente:
        content = db.Cliente.to_dict(cliente)
        return JSONResponse(content=content, headers=headers)
    else:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    

@app.post("/clientes", tags = ["Clientes"])
async def crear_cliente(cliente: Modelo_de_Cliente):
    cliente = db.Cliente(cliente.id, cliente.nombre, cliente.apellido, cliente.dni)
    if cliente:
        return JSONResponse(content=db.Cliente.to_dict(), headers=headers)
    else:
        raise HTTPException(status_code=404, detail="Cliente no creado")
    


@app.put("/clientes/{id}", tags = ["Clientes"])
async def actualizar_cliente(id: int, cliente: Modelo_de_Cliente):
    cliente = db.Cliente(cliente.id, cliente.nombre, cliente.apellido, cliente.dni)
    if cliente:
        return JSONResponse(content=db.Cliente.to_dict(), headers=headers)
    else:
        raise HTTPException(status_code=404, detail="Cliente no actualizado")
    

@app.delete("/clientes/{id}", tags = ["Clientes"])
async def eliminar_cliente(id: int):
    cliente = db.Clientes.buscar(id)
    if cliente:
        db.Clientes.borrar(cliente)
        return JSONResponse(content=db.Cliente.to_dict(), headers=headers)
    else:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
