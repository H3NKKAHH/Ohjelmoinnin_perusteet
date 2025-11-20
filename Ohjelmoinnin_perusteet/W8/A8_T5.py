import user_manager


logged_in_user = None 

def show_main_options():
    print("Options:")
    print("1 -  Login")
    print("2 -  Register")
    print("0 - Exit")

def show_user_options(username):
    
    print("User menu:")
    print("1 -  View profile")
    print("2 - Change password")
    print("0 - Logout")

def main():
    
    global logged_in_user 
    
    print("Program starting.")
    
    while True:
        
        
        if logged_in_user is None:
            show_main_options()
            choice = input("Your choice: ")
            
            if choice == "1":
                username = input("Insert username: ")
                password = input("Insert password: ")
                
                hashed_pw = user_manager.hash_password(password)
                success, user_info = user_manager.authenticate_user(username, hashed_pw)
                
                if success:
                    user_id, user_name = user_info
                    
                    logged_in_user = {'id': user_id, 'username': user_name} 
                    print("Authentication successful!")
                else:
                    print("Authentication failed!")
                    
            elif choice == "2":
                username = input("Insert username: ")
                password = input("Insert password: ")
                
                hashed_pw = user_manager.hash_password(password)
                user_manager.register_user(username, hashed_pw)
                
                print("User registration completed!")
                
            elif choice == "0":
                break
                
        else:
            show_user_options(logged_in_user['username'])
            user_choice = input("Your choice: ")
            
            if user_choice == "1":
                user_id = logged_in_user['id']
                user_name = logged_in_user['username']
                print(f"Profile ID {user_id} - {user_name}")
            
            elif user_choice == "2":
                print("Functionality not implemented.")
            
            elif user_choice == "0":
                
                logged_in_user = None 
                print("Logging out...")
            
        print()

if __name__ == "__main__":
    main()
    print("")
    print("Program ending.")