from db.models import Ingredient
from sqlalchemy.orm import Session
def add_ingredient(db: Session, name: str, stock: int):
    """Add a new ingredient to the inventory using SQLAlchemy ORM."""
    try:

        existing_ingredient = db.query(Ingredient).filter(Ingredient.name == name).first()
        if existing_ingredient:
            print(f"'{name}' already exists...")
            return

        new_ingredient = Ingredient(name=name, stock=stock)
        db.add(new_ingredient)
        db.commit()
        db.refresh(new_ingredient)
        print(f"{name} added successfully with stock: {stock}...")

    except Exception as e:

        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()
