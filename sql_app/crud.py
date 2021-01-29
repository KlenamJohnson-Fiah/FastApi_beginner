from sqlalchemy.orm import Session
#from . import model,scheme

import model
import scheme

from typing import Optional


def get_owner(db: Session,owner_id: int):
    return db.query(model.Owner).filter(model.Owner.id == owner_id).first()

def get_pet(db : Session,pet_id: int):
    return db.query(model.Pet).filter(model.Pet.id == pet_id).first()

def get_pets_using_ownerName(db: Session, owner_name: str):
    pets_identified = db.query(model.Pet).filter(model.Pet.owner == owner_name).all()
    return pets_identified

def create_owner(db: Session, owner: scheme.OwnerCreation):
    #db_owner = model.Owner(owner_name= owner.name, phone_number= owner.phoneNumber, place_of_residence= owner.placeOfResidence)
    db_owner = model.Owner(**owner.dict())
    db.add(db_owner)
    db.commit()
    db.refresh(db_owner)
    return db_owner

def create_pet(db:Session, pet:scheme.PetCreation):
    #db_pet = model.Pet(pet_name= pet.pet_name, pet_type= pet.pet_type)
    db_pet = model.Pet(**pet.dict())
    db.add(db_pet)
    db.commit()
    db.refresh(db_pet)
    return db_pet