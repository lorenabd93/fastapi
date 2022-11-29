#from typing import List
from uuid import uuid4

from pydantic import BaseModel

from fastapi import FastAPI

app = FastAPI()

class Vehiculo(BaseModel):
	id: str
	name: str
	lastname: str
	#skills: List[str] = []

vehiculos = []

@app.get("/vehiculos")

def get_vehiculos():
	return vehiculos
@app.get("/vehiculos/{id}")
def get_vehiculo(id: str):
	for vehiculo in vehiculos:
		if vehiculo["id"] == id:
			return vehiculo
	return "No existe el vehiculo"
   

@app.post("/vehiculos")
def save_vehiculo(vehiculo: Vehiculo):
	vehiculo.id = str(uuid4())
	vehiculos.append(vehiculo.dict())
	return "Vehiculo registrado"

@app.put("/vehiculos/{id}")
def update_vehiculo(updated_updated: Vehiculo, id:str):
	for vehiculo in vehiculos:
		if vehiculo["id"] == id:
			vehiculo["name"] = updated_updated.name
			vehiculo["lastname"] = updated_updated.lastname
			#vehiculo["skills"] = updated_updated.skills
			return "Vehiculo modificado"
	return "No existe el vehiculo"

@app.delete("/vehiculos/{id}")
def delete_vehiculo(id: str):
	for vehiculo in vehiculos:
		if vehiculo["id"] == id:
			vehiculos.remove(vehiculo)
			return "Vehiculo eliminado"
	return "No existe el vehiculo"