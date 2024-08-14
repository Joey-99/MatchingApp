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
    gender = input("Please enter your gender ('M' for male, 'F' for female, 'O' for other): ").upper()
    while True:
        try:
            if gender != 'M' and gender != 'F' and gender != 'O':
                raise ValueError
            break
        except Exception:
            gender = input("Gender error, please enter your gender ('M' for male, 'F' for female, 'O' for other): ").upper()
    return gender

def get_user_location():
    location = input("Please enter your location: ")
    return location

def get_preferred_genders():
    gender_interest = input("Please enter which genders you are interested in (i.e. 'MF' for male and female, 'MFO' for all, and 'F' for just female): ").strip().upper()
    while not set(gender_interest).issubset({'M', 'F', 'O'}) or len(gender_interest) != len(set(gender_interest)):
        gender_interest = input("Invalid genders, please enter 'M' for male, 'F' for female, or 'O' for other: ").strip().upper()
    return gender_interest

def get_age_limit():
    age_limit = input("Please enter the upper age limit you can accept (i.e. 30 for 30 years old, 50 for 50 years old, None for no age limit: ")
    if age_limit == 'None':
        return age_limit
    while not age_limit.isdigit():
        age_limit = input("Invalid age input, please enter the upper age limit you can accept (i.e. 30 for 30 years old, 50 for 50 years old, None for no age limit: ")
    return age_limit

def get_like_dislike():
    like = input("Please enter whether you like or dislike this person ('like' or 'dislike' or 'exit'): ").lower()
    while like != 'like' and like != 'dislike' and like != 'exit':
        like = input("Invalid entry, please enter whether you like or dislike this person ('like' or 'dislike' or 'exit'): ").lower()
    return like

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
            preferred_genders = get_preferred_genders()
            age_limit = get_age_limit()

            user1 = user.create_user(username, password, name, age, gender, location, [], preferred_genders, age_limit)
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

        user_id = user.get_user_id(username)

        while logged_in:
            option = input("Please choose an option (browse_profiles OR view_matches OR edit_profile OR logout OR delete_profile): ").lower()
            if option == 'logout':
                logged_in = False
                break
            elif option == 'browse_profiles':
                interests = user.get_interests(user_id)
                interests_shuffled = interests.sample(frac=1).reset_index(drop=True)
                for other_user_id in interests_shuffled['user_id'].tolist():
                    print(interests_shuffled[interests_shuffled['user_id'] == other_user_id])
                    like = get_like_dislike()
                    if like == 'exit':
                        continue
                    elif like == 'like':
                        user.like_profile(user_id, other_user_id)
                    elif like == 'dislike':
                        user.dislike_profile(user_id, other_user_id)
                print('You have viewed all profiles, please check again later for more.')
            elif option == 'view_matches':
                print('You have matched with the following users')
                matches = user.evaluate_matches(user_id)
                print(matches)
            elif option == 'delete_profile':
                user.delete_user_from_db(user_id)
                success_delete = user.check_valid_username(username)
                if success_delete:
                    logged_in = False
                    break
                else:
                    continue
            elif option == 'edit_profile':
                # show options for changing user profile fields (password, name, age, gender, location)
                None
