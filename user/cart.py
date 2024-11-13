from db.models import Cart, Flavor  
from db.database import get_db  

db = next(get_db())

# Function to add an item to the cart
def add_to_cart():
    """Add an item (flavor) to the cart with specified quantity and optional topping."""
    try:
        item = input("Enter the flavor name: ").strip()  
        quantity = int(input("Enter quantity: "))
        topping = input("Enter topping (or press Enter to skip): ").strip()

        flavor = db.query(Flavor).filter(Flavor.name.ilike(item)).first()  # case-insensitive chek
        if not flavor:
            print(f"Flavor '{item}' does not exist. Please try again.")
            return

        cart_item = Cart(item=item, quantity=quantity, topping=topping)
        db.add(cart_item)
        db.commit()  
        print(f"Item '{item}' added to cart with quantity {quantity} and topping '{topping}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()  
    finally:
        db.close()  

def view_cart():
    """Display all items currently in the cart."""
    try:
        cart_items = db.query(Cart).all()  
        if not cart_items:
            print("Your cart is empty.")
            return
        
        print("Your Cart:")
        for item in cart_items:
            print(f"ID: {item.id}, Item: {item.item}, Quantity: {item.quantity}, Topping: {item.topping}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()


def update_cart_items():
    """Modify the quantity or topping of an existing cart item by ID."""
    try:
        cart_item_id = int(input("Enter the cart item ID to modify: "))
        cart_item = db.query(Cart).filter(Cart.id == cart_item_id).first() 
        
        if not cart_item:
            print(f"Cart item with ID {cart_item_id} not found.")
            return

        # new deets
        new_quantity = input("Enter new quantity (or press Enter to keep current): ").strip()
        new_topping = input("Enter new topping (or press Enter to keep current): ").strip()
        
        if new_quantity:
            cart_item.quantity = int(new_quantity)
        if new_topping:
            cart_item.topping = new_topping

        db.commit()  
        print(f"Cart item with ID {cart_item_id} has been updated.")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()  
    finally:
        db.close()


def remove_from_cart():
    """Remove a cart item by its ID."""
    try:
        cart_item_id = int(input("Enter the cart item ID to remove: "))
        cart_item = db.query(Cart).filter(Cart.id == cart_item_id).first()  # Find cart item by ID
        
        if not cart_item:
            print(f"Cart item with ID {cart_item_id} not found.")
            return

        db.delete(cart_item)  # Delete the cart item
        db.commit()  # Commit the changes
        print(f"Cart item with ID {cart_item_id} has been removed from the cart.")
    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()  # Rollback in case of error
    finally:
        db.close()
