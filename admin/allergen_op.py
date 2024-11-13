from db.models import Allergen
from sqlalchemy.orm import Session
def add_allergen(db: Session, name: str):
    """Add a new allergen to the database """
    try:
        # Check if allergen already exists
        existing_allergen = db.query(Allergen).filter(Allergen.name == name).first()
        if existing_allergen:
            print(f"Allergen '{name}' already exists.")
            return

        new_allergen = Allergen(name=name)
        db.add(new_allergen)
        db.commit()
        db.refresh(new_allergen)
        print(f"Allergen '{name}' added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()