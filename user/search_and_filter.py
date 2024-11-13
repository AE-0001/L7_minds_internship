from sqlalchemy import func
from db.models import Flavor
from db.database import get_db



def search_and_filter():
    """Allow the user to search and filter the ice cream offerings."""
    db = next(get_db())
    try:
        # Get the user's search input for flavor name or description
        search = input("Enter a keyword to search flavors (name or description): ").strip()

        # Get the user's choice to filter by seasonal flavors
        filter_seasonal = input("Do you want to filter by seasonal flavors? (yes/no): ").strip().lower()

        # Create the base query
        query = db.query(Flavor)

        # Apply the search filter for case-insensitive exact match
        if search:
            query = query.filter(
                (func.lower(Flavor.name).like(f"%{search.lower()}%")) | 
                (func.lower(Flavor.description).like(f"%{search.lower()}%"))
            )

        # Apply the seasonal filter if specified by the user
        if filter_seasonal == "yes":
            query = query.filter(Flavor.is_seasonal == True)

        # Execute the query and retrieve results
        results = query.all()

        # Display the results to the user
        if not results:
            print("No flavors matched your search criteria.")
        else:
            print("Available flavors:")
            for flavor in results:
                seasonal_desc = "Seasonal" if flavor.is_seasonal else "Regular"
                print(f"Name: {flavor.name}, Description: {flavor.description}, Type: {seasonal_desc}")

    except Exception as e:
        print(f"An error occurred while searching: {e}")
    finally:
        db.close()

# Example call to the function
if __name__ == "__main__":
    search_and_filter()
