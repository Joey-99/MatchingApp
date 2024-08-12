from user_management_new import user_management_new

def get_user_name():
    name = input("Please enter your name: ")
    return name

def get_user_age():
    age = input("Please enter your age (1-100): ")
    while True:
        try:
            age = int(age)
            if age < 1 or age > 100:
                raise ValueError
            break
        except Exception:
            age = input("Age error, please enter your age (1-100): ")
    return age

def get_user_gender():
    gender = input("Please enter your gender (M for male, F for female, O for other): ")
    while True:
        try:
            if gender != 'M' and gender != 'F' and gender != 'O':
                raise ValueError
            break
        except Exception:
            gender = input("Gender error, please enter your gender (M for male, F for female, O for other): ")
    return gender

def get_user_location():
    location = input("Please enter your location: ")
    return location

if __name__ == '__main__':
    # Instantiate the user object
    user = user_management_new()
    
    while True:
        # receive input commands
        logged_in = False
        cmd = input("Please enter the command (login OR create_account): ").lower()
        
        # exit commands
        if cmd == 'create_account':
            username = input("Please enter a username (minimum length of 5 characters): ")
            valid = user.check_valid_username(username)
            while not valid or len(username) < 5:
                if len(username) < 5:
                    username = input("Username must be a minimum of 5 characters: ")
                else:
                    username = input(f"The username '{username}' already exists, please try again (minimum length of 5 characters): ")
                    valid = user.check_valid_username(username)
            password = input("Please enter a password (minimum length of 5 characters): ")
            while len(password) < 5:
                password = input("Password must be a minumum of 5 characters: ")
            
            name = get_user_name()
            age = get_user_age()
            gender = get_user_gender()
            location = get_user_location()

            user1 = user.create_user(username, password, name, age, gender, location, [])
            user.add_user_to_db(user1)
            logged_in = True
        
        elif cmd == 'login':
            username = input("Please enter your username: ")
            user_exists = not user.check_valid_username(username)
            while not user_exists:
                username = input(f"The username '{username}' does not exists, please try again: ")
                user_exists = not user.check_valid_username(username)
            actual_password = user.get_user_password(username)
            password = input("Enter your password: ")
            while password != actual_password:
                password = input("The password you entered is incorrect, please try again: ")
            logged_in = True

        else:
            print("Not a valid command, please try again.")
            continue

        while logged_in:
            option = input("Please choose an option (browse_profiles OR view_matches OR edit_profile OR logout): ").lower()
            if option == 'logout':
                logged_in = False
                break
            elif option == 'browse_profiles':
                # show the strongest matches for the particular user
                None
            elif option == 'view_matches':
                # show all matches for the particular user
                None
            elif option == 'edit_profile':
                # show options for changing user profile fields (password, name, age, gender, location)
                None
