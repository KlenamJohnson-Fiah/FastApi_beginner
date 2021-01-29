from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Pet(Base):
    __tablename__= "pets"

    id = Column(Integer, primary_key=True, index= True)
    pet_name = Column(String, index=True)
    pet_type = Column(String)
    illness = Column(String)
    remedy = Column(String)
    owner = Column(String)
    owner_id = Column(String, ForeignKey("owners.id"))
  
    
class Owner(Base):
    __tablename__= "owners"

    id = Column(Integer,primary_key=True, index=True)
    owner_name= Column(String)
    phone_number = Column(Integer)
    place_of_residence = Column(String)
    
