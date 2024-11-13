from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Flavor(Base):
    __tablename__ = 'flavors'


    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_seasonal = Column(Boolean, default=False)


class Ingredient(Base):
    __tablename__= 'ingredients'


    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    stock = Column(Integer, nullable=False)


class Allergen(Base):
    __tablename__= 'allegens'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)


class Suggestflavor(Base):
    __tablename__='Suggest_flavor'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    is_approved = Column(Boolean, default=False)
    is_seasonal = Column(Boolean, default=False)

class Cart(Base):
    __tablename__ = 'Cart'

    id = Column(Integer, primary_key=True, autoincrement=True)
    item = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    topping = Column(String, nullable=True)


