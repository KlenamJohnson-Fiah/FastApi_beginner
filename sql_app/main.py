from fastapi import FastAPI,Depends,HTTPException,Path
#from . import model,scheme,crud

import crud
import model
import scheme

from sqlalchemy.orm import Session
from database import SessionLocal,engine

from typing import List

from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

model.Base.metadata.create_all(bind=engine)

app=FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

@app.post("/pet/", response_model= scheme.PetCreation)
def create_pet(pet: scheme.PetCreation, db:Session= Depends(get_db)):
    db_pet = crud.create_pet(db=db, pet=pet)
    return db_pet

@app.get("/pet/{pet_id}/", response_model = scheme.Pet)
def read_pet(pet_id:int=Path(...),db:Session=Depends(get_db) ):
    db_pet = crud.get_pet(db, pet_id=pet_id)
    if db_pet is None:
        raise HTTPException(status_code=404, detail="Pet not Found")
    return db_pet


@app.post("/owner/", response_model= scheme.OwnerCreation)
def create_owner(owner: scheme.OwnerCreation, db: Session=Depends(get_db)):
    db_owner = crud.create_owner(db=db, owner=owner)
    return db_owner

@app.get("/owner/{owner_name}/", response_model = List[scheme.Pet])
def read_pet_using_user_name(owner_name:str=Path(...), db: Session = Depends(get_db)):
    db_owner = crud.get_pets_using_ownerName(db=db, owner_name=owner_name)
    if db_owner==[] :
        raise HTTPException(status_code=404, detail="can't find pets with that name")
    return db_owner
