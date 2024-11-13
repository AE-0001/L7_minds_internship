from sqlalchemy import func
from db.models import Suggestflavor, Flavor
from db.database import get_db

db = next(get_db())

def suggest_flav():
    try:
        name=input("Enter an interesting flavour ypu want to suggest, we will review and add it to the menu!").strip()
        description= input("Enter the flavor description: ").strip()

        existing_flavor = db.query(Flavor).filter(func.lower(Flavor.name) == func.lower(name)).first()
        existing_flavor_in_pending = db.query(Suggestflavor).filter(func.lower(Suggestflavor.name) == func.lower(name)).first()

        if existing_flavor:
            print(f"The flavor '{name}' already exists in the database.")
        elif existing_flavor_in_pending:
            print(f"The flavor '{name}' is already pending for approval.")
           
        else:
            # If the flavor doesn't exist, create a new one
            new_flavor = Suggestflavor(name=name, description=description) #is_seasonal=is_seasonal)
            db.add(new_flavor)
            db.commit()
            print(f"Flavor '{name}' awaiting for approval!")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()  # Rollback the transaction in case of error
    finally:
        db.close()  # Close the session

# Example usage in the menu or main program
if __name__ == "__main__":
    suggest_flav()