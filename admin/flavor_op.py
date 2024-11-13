from db.models import Flavor
from sqlalchemy.orm import Session

def add_flavor(db: Session, name: str, description: str, is_seasonal: bool):
    """Add a new flavor to the database using SQLAlchemy ORM."""
    try:
        #checking existing deets
        existing_flavor = db.query(Flavor).filter(Flavor.name == name).first()
        if existing_flavor:
            print(f"Flavor '{name}' already exists.")
            return

        new_flavor = Flavor(name=name, description=description, is_seasonal=is_seasonal)
        db.add(new_flavor)
        db.commit()
        db.refresh(new_flavor)
        print(f"Flavor '{name}' added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()
    finally:
        db.close()