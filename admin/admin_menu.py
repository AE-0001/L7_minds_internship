from admin.flavor_op import add_flavor
from admin.ingredient_op import add_ingredient
from admin.allergen_op import add_allergen
from admin.approve_flavor_suggestion import approve_flavors
from db.database import get_db

db = next(get_db())

def get_flavor():
    """Prompt user to add a new flavor."""
    name = input("Flavor name: ")
    description = input("Description: ")
    is_seasonal = input("Is it seasonal? (yes/no): ").strip().lower() == 'yes'
    add_flavor(db, name, description, is_seasonal, )

def get_ingredient():
    """Prompt user to add a new ingredient."""
    name = input("Ingredient name: ")
    stock = int(input("Stock amount: "))
    add_ingredient(db, name, stock)

def get_allergen():
    """Prompt user to add a new allergen."""
    name = input("Allergen name: ")
    add_allergen(db, name)

def admin_menu():
    """Display main menu options and handle user input."""
    options = {
        '1': ("Add Flavor", get_flavor),
        '2': ("Add Ingredient", get_ingredient),
        '3': ("Approve Flavor", approve_flavors),  # Assume function `add_suggestion_prompt` exists
        '4': ("Add Allergen", get_allergen),
        '5': ("Exit", exit)
    }

    while True:
        print("\nWelcome to the Ice Cream Parlor Cafe!\nOptions:")
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        
        choice = input("Select an option (1-6): ")
        action = options.get(choice)

        if action:
            action[1]()  # Call the corresponding function
        else:
            print("Invalid option. Please choose a valid option.")
