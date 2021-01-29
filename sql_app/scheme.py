from pydantic import BaseModel

from typing import Optional,List



class OwnerBase(BaseModel):
    owner_name: str


class OwnerCreation(OwnerBase):
    place_of_residence : Optional[str]
    phone_number : int

    class Config:
         orm_mode = True


class Owner(OwnerCreation):
    id : int
    pets : List[str]
    
    class Config:
         orm_mode = True



class PetBase(BaseModel):
    pet_type : str
    pet_name : str

class PetCreation(PetBase):
    owner : str
    #dog_registration_ID : str

    class Config:
         orm_mode = True


class Pet(PetCreation):
    id :int

    class Config:
         orm_mode = True

    




