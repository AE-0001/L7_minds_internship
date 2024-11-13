from db.models import Suggestflavor, Flavor
from db.database import get_db

def approve_flavors():
    """Admin to review pending flavors and approve them."""
    db = next(get_db()) 

    try:
        # pending flvaros (not yet approved)
        pending_suggested_flavors = db.query(Suggestflavor).filter(Suggestflavor.is_approved == False).all()

        if not pending_suggested_flavors:
            print("No pending suggested flavors for approval!!!...")
            return
        
        # Display pending suggested flavors
        print("Pending Suggested Flavors for Admin Approval:")
        for flavor in pending_suggested_flavors:
            print(f"\n\n\nID: {flavor.id}, Name: {flavor.name}, Description: {flavor.description}, Seasonal: {flavor.is_seasonal}!!!!!...")

        # Get the approvalfrom admin
        flavor_id = int(input("\n \nEnter the ID of the flavor you want to approve/reject: "))
        approval = input("\n\nDo you approve this flavor? (yes/no): ").strip().lower()

        flavor_to_approve = db.query(Suggestflavor).filter(Suggestflavor.id == flavor_id).first()

        if not flavor_to_approve:
            print("Flavor ID not found.")
            return
        
        if approval == "yes":
            # Move the flavor to the main Flavor table and approve it
            new_flavor = Flavor(name=flavor_to_approve.name, description=flavor_to_approve.description, is_seasonal=flavor_to_approve.is_seasonal)
            db.add(new_flavor)
            flavor_to_approve.is_approved = True  # Mark as approved
            db.commit()
            print(f"Flavor '{flavor_to_approve.name}' has been approved and added to the main menu.")
        else:
            # Reject the flavor and remove from pending list
            db.delete(flavor_to_approve)
            db.commit()
            print(f"Flavor '{flavor_to_approve.name}' has been rejected.")

    except Exception as e:
        print(f"An error occurred: {e}")
        db.rollback()  # Rollback the transaction in case of error
    finally:
        db.close()  # Close the session
