from db.models import Allergen
from db.database import get_db

db = next(get_db())

def get_allergens():
    try:
        add_allergen=input("Enter allergens if any").strip()

        if add_allergen:
            
            existing_allergen=db.query(Allergen).filter(Allergen.name.like(f"%{add_allergen.lower()}")).first()
            

        if not existing_allergen:
            new_allergen=Allergen(name=add_allergen.lower())
            db.add(new_allergen)
            db.commit()
            print(f"\n\nAllergen '{new_allergen.name}' added. Thank you for letting us know!...")
        else:
            print(f"\n\nAllergen '{existing_allergen.name}' already exists in our database.")

    except Exception as e:
        print("An error occurred ", e)
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    get_allergens()