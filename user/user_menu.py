from user.cart import add_to_cart, display_cart, modify_cart_item, remove_from_cart
from user.add_allergen import get_allergens
from user.search_and_filter import search_and_filter_offerings
from user.suggest_flavor import suggest_flav
def view_menu():
    print("\nWelcome to L7 Ice cream parlor cafe")
    print("Select an option from the menu below:")
    print("\n*** Ice Cream Cart ***")
    print("1. Add item to cart")
    print("2. View cart")
    print("3. Modify cart item")
    print("4. Remove item from cart")
    print("5. Search n filter")
    print("6. Add allergens")
    print("7. Suggest flavor")
    print("8. Exit")

def user_interface():
    while True:

        view_menu()
        try:

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_to_cart()
            elif choice == "2":
                display_cart()
            elif choice == "3":
                modify_cart_item()
            elif choice == "4":
                remove_from_cart()
            elif choice == "5":
                search_and_filter_offerings()
            elif choice == "6":
                get_allergens()
            elif choice == "7":
                suggest_flav()
            elif choice== "8":
                print("Exiting user interface...")
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid choice enter number between 1 and 7")
if __name__ == '__main__':

    user_interface()
