from user.user_menu import user_menu
from admin.admin_menu import admin_menu

if __name__ == '__main__':
    roles ={1:"Admin", 2:"User"}
    print("Welcome to L7 Ice cream parlor cafe!!!...\n\nEnter your role...")
    role=int(input())
    if role == 1:
        admin_menu()
    else:
        user_menu()





    