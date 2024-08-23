import GUI
from user_management_new import user_management_new

COLUMNS_TO_SHOW = ['name', 'age', 'gender', 'location', 'education', 'interests', 'politics', 'intentions']

def get_username():
    '''
    Cmd line function that prompts the user for a username
    Verifies that the username does not already exist in the table
    '''
    username = input("\nPlease enter a username (minimum length of 5 characters): ")
    valid = user.check_valid_username(username)
    while not valid or len(username) < 5:
        if len(username) < 5:
            username = input("Username must be a minimum of 5 characters: ")
        else:
            username = input(f"The username '{username}' already exists, please try again (minimum length of 5 characters): ")
            valid = user.check_valid_username(username)
    return username

def get_user_name():
    '''
    Cmd line function that prompts the user for their name
    '''
    name = input("\nPlease enter your name: ")
    return name

def get_user_age():
    '''
    Cmd line function that prompts the user for their age
    Verifies the age is an integer and valid
    '''
    age = input("\nPlease enter your age (18-100): ")
    while True:
        try:
            age = int(age)
            if age < 18 or age > 100:
                raise ValueError
            break
        except Exception:
            age = input("Age error, please enter your age (18-100): ")
    return age

def get_user_feature_weights():
    '''
    Cmd line function that prompts a user for their feature importance
    Verifies each weight is set to an int between 1 and 10
    Adds an additional element as the max of the previous weights as the importance of the feature: if a user likes me
    '''
    print('Please enter a rating of 1-10 for the following user attributes: age, interests, location, education, politics, and dating intentions')
    print("If you wish to use default equal weights, please enter 'done'")
    features = ['Age', 'Interests', 'Location', 'Education', 'Politics', 'Dating Intentions']
    weights = []
    for feature in features:
        weight = input(f'{feature}: ')
        if weight.strip().lower() == 'done':
            weights = [5,5,5,5,5,5,5]
            return weights
        while True:
            try:
                weight = int(weight)
                if weight < 1 or weight > 10:
                    raise ValueError
                break
            except Exception:
                weight = input("Feature weight error, please enter a weight from 1-10: ")
        weights.append(weight)
    max_weight = max(weights)
    weights.append(max_weight)
    return weights 

def get_user_gender():
    '''
    Cmd line function that prompts the user for their gender
    Verifies a valid gender is provided
    '''
    gender = input("\nPlease enter your gender ('M' for male, 'F' for female, 'O' for other): ").upper()
    while True:
        try:
            if gender != 'M' and gender != 'F' and gender != 'O':
                raise ValueError
            break
        except Exception:
            gender = input("Gender error, please enter your gender ('M' for male, 'F' for female, 'O' for other): ").upper()
    return gender

def get_political_view():
    '''
    Cmd line function that prompts the user for their political views
    Verifies a valid political view is provided
    '''
    politics = input("\nPlease enter your political orientation ('L' for liberal, 'C' for conservative, 'N' for neutral): ").upper()
    while True:
        try:
            if politics != 'L' and politics != 'C' and politics != 'N':
                raise ValueError
            break
        except Exception:
            politics = input("Political orientation error, please enter your political orientation ('L' for liberal, 'C' for conservative, 'N' for neutral): ").upper()
    return politics

def get_dating_intentions():
    '''
    Cmd line function that prompts the user for their dating intentions
    Verifies the intention provided
    '''
    intentions = input("\nPlease enter your dating intentions ('S' for short-term, 'L' for long-term, 'C' for casual, 'LP' for life partner): ").upper()
    while True:
        try:
            if intentions != 'S' and intentions != 'L' and intentions != 'C' and intentions != 'LP':
                raise ValueError
            break
        except Exception:
            intentions = input("Dating intentions error, please enter your dating intentions ('S' for short-term, 'L' for long-term, 'C' for casual, 'LP' for life partner): ").upper()
    return intentions

def get_user_location():
    '''
    Cmd line function that prompts the user for their location
    Verifies the location is part of a set of predetermined locations
    '''
    location = input("\nPlease enter your location one of your cities in Ontario, Canada: ").strip(",._ ")
    ontario_cities = [
    "Toronto",
    "Ottawa",
    "Mississauga",
    "Brampton",
    "Hamilton",
    "London",
    "Markham",
    "Vaughan",
    "Kitchener",
    "Windsor",
    "Richmond Hill",
    "Burlington",
    "Oshawa",
    "Greater Sudbury",
    "Barrie",
    "Guelph",
    "Cambridge",
    "St. Catharines",
    "Waterloo",
    "Thunder Bay",
    "Brantford",
    "Pickering",
    "Niagara Falls",
    "Peterborough",
    "Sault Ste. Marie",
    "Sarnia",
    "Norfolk County",
    "Welland",
    "Belleville",
    "North Bay"
]
    while location not in ontario_cities:
        location = input("Invalid Location, please enter your location: ").strip(",._ ")
    return location

def get_user_education_level():
    '''
    Cmd line function that prompts the user for their education level
    Verifies the education provided is a valid entry
    '''
    education = input("\nPlease enter your education level as following ['highschool', 'bachelor', 'master', 'phd']: ").strip(",._ ").lower()
    while education not in ['highschool', 'bachelor', 'master', 'phd']:
        education = input("Invalid education level, please enter your education level as following ['highschool', 'bachelor', 'master', 'phd']: ").strip(",._ ").lower()
    return education

def get_preferred_genders():
    '''
    Cmd line function that prompts the user for their gender preference
    Verifies the preferences provided are valid entries
    '''
    gender_interest = input("\nPlease enter which genders you are interested in (i.e. 'MF' for male and female, 'MFO' for all, and 'F' for just female): ").strip().upper()
    while not set(gender_interest).issubset({'M', 'F', 'O'}) or len(gender_interest) != len(set(gender_interest)):
        gender_interest = input("Invalid genders, please enter which genders you are interested in (i.e. 'MF' for male and female, 'MFO' for all, and 'F' for just female): ").strip().upper()
    return gender_interest

def get_age_range():
    '''
    Cmd line function that prompts the user for their preferred age range
    Verifies the age range provided is ints and valid
    '''
    while True:
        age_range_input = input("\nPlease enter the ages you are interest in (e.g., 25-100): ")

        try:
            age_min, age_max = map(int, age_range_input.split('-'))
            if 1 <= age_min <= 100 and 1 <= age_max <= 100 and age_min < age_max:
                return age_min, age_max
            else:
                print("Error: Please ensure both numbers are between 1 and 100, and the first number is smaller than the second.")
        except ValueError:
            print("Error: Please enter the range in the correct format (e.g., 25-100).")

def get_like_dislike():
    '''
    Cmd line function that prompts the user for liking/disliking a profile
    Verifies the entry is valid
    '''
    like = input("\nPlease enter whether you like or dislike this person ('like' or 'dislike' or 'exit'): ").lower()
    while like != 'like' and like != 'dislike' and like != 'exit':
        like = input("Invalid entry, please enter whether you like or dislike this person ('like' or 'dislike' or 'exit'): ").lower()
    return like

def get_password():
    '''
    Cmd line function that prompts the user for a password
    Verifies the entry is valid
    '''
    password = input("\nPlease enter a password (minimum length of 5 characters): ")
    while len(password) < 5:
        password = input("Password must be a minumum of 5 characters: ")
    return password

def get_user_interests():
    '''
    Cmd line function that prompts the user for a list of interests
    Verifies the interests provided belong to a predetermined list
    Ensures no duplicates using a set when saving the interests to the db
    '''
    Selecting = True
    interests_list = []

    while Selecting:
        interest = input("""\nPlease choosing interests from the following options, select one at a time, type done to finish selection [
        "music", "movies", "sports", "reading", "travel", "hiking", "cooking", "gaming", "gardening"]: """).strip(",._ ").lower()
        if interest.lower() == 'done':
            Selecting = False
            continue
        while  interest.lower() not in ["music", "movies", "sports", "reading", "travel", "hiking", "cooking", "gaming", "gardening"]:
            interest = input("Invalid interest, please choose from the following options: ").strip(",._ ").lower()
        interests_list.append(interest)
        
    return list(set(interests_list))

if __name__ == '__main__':
    # Instantiate the user object
    user = user_management_new()
    
    while True:
        # receive initial input commands
        logged_in = False
        cmd = input("\nPlease enter the command (login OR create_account OR gui OR exit): ").lower()
        
        if cmd == 'create_account':
            # if the user wishes to create an account - provide them all the prompts and save the information
            username = get_username()
            password = get_password()
            name = get_user_name()
            age = get_user_age()
            gender = get_user_gender()
            location = get_user_location()
            education = get_user_education_level()
            interests = get_user_interests()
            politics = get_political_view()
            intentions = get_dating_intentions()
            preferred_genders = get_preferred_genders()
            age_low, age_high = get_age_range()
            weights = get_user_feature_weights()

            # create a user object with the required information
            user1 = user.create_user(username, password, name, age, gender, location, education, interests, politics, intentions, preferred_genders, age_low, age_high, weights)
            # save the user information to the db
            user.add_user_to_db(user1)
            print(f'\nWelcome {username}! :) Please select an option from the list below to get started:')
            logged_in = True
        
        elif cmd == 'login':
            # if the user is attempting to login, collect their username and password
            # verify the username already exists
            username = input("\nPlease enter your username: ")
            user_exists = not user.check_valid_username(username)
            while not user_exists:
                username = input(f"The username '{username}' does not exists, please try again: ")
                user_exists = not user.check_valid_username(username)
            actual_password = user.get_user_password(username)
            password = input("\nEnter your password: ")
            # verify the password entered matches the stored password for that user
            while password != actual_password:
                password = input("The password you entered is incorrect, please try again: ")
            print(f'\nWelcome back {username}! :) Please select an option from the list below to get started:')
            logged_in = True
        
        elif cmd == 'gui':
            # if gui - provide all options through the gui interface
            GUI.start()
            # exit program after closing gui
            exit(0)
        
        elif cmd == 'exit':
            # exit the program
            exit(0)

        else:
            print("Not a valid command, please try again.")
            continue

        # get the user_id of the logged in user
        user_id = user.get_user_id(username)

        while logged_in:
            # provide the user with the available menu options
            option = input("\nPlease choose an option (browse_profiles OR view_matches OR edit_profile OR logout OR delete_profile OR view_all_profiles): ").lower()
            
            if option == 'logout':
                # if logout - go back to the main login page
                logged_in = False
                break
            
            elif option == 'browse_profiles':
                # if browse profiles, collect all ranked potential matches for the user
                interests = user.get_potentials(user_id)
                exit = False
                for other_user_id in interests['user_id'].tolist():
                    # display the user's sequantially based on their score
                    if exit:
                        break
                    print(interests[interests['user_id'] == other_user_id][COLUMNS_TO_SHOW])
                    # get a like/dislike input from the user
                    # allow them to exit back to the main menu
                    like = get_like_dislike()
                    matches_before = user.number_of_matches(user_id)
                    if like == 'exit':
                        exit = True
                        continue
                    elif like == 'like':
                        user.like_profile(user_id, other_user_id)
                    elif like == 'dislike':
                        user.dislike_profile(user_id, other_user_id)
                    matches_after = user.number_of_matches(user_id)
                    if matches_after > matches_before:
                        print('\n\nYou have a new match! Visit your matches from the main menu!\n\n')
                if not exit:
                    # if they have viewed all potential matches, relay the information and return to the main menu
                    print('\nYou have viewed all profiles, please check again later for more.')
            
            elif option == 'view_matches':
                # if view matches - show the user all users they have matched with (mutually liked)
                matches = user.evaluate_matches(user_id)
                if len(matches) == 0:
                    print('\nYou have no matches at this time, keep liking profiles :)')
                else:
                    print('\nYou have matched with the following users\n')
                    print(matches[COLUMNS_TO_SHOW])
            
            elif option == 'delete_profile':
                # if delete profile - verify the user is sure they wish to delete their profile
                sure = input('\nAre you sure you want to delete your profile (Y/N): ').upper()
                while sure != 'Y' and sure != 'N':
                    sure = input('Invalid input, are you sure you want to delete your profile (Y/N): ').upper()
                # if yes - delete the user from the database
                if sure == 'Y':
                    user.delete_user_from_db(user_id)
                    success_delete = user.check_valid_username(username)
                    print('We are sad to see you go :(')
                    if success_delete:
                        logged_in = False
                        break
                    else:
                        continue
                # if no - go back to the main menu
                elif sure == 'N':
                    continue
            
            elif option == 'edit_profile':
                # if edit profile - provide the user with all fields they are able to edit
                edit_option = input('\nWhich profile field would you like to update (username, password, name, age, gender, location, education, politics, intentions, interests, preferred_genders, preferred_age, weights): ')
                while edit_option not in ['username', 'password', 'name', 'age', 'gender', 'location', 'education', 'preferred_genders', 'preferred_age', 'interests', 'politics', 'intentions', 'weights']:
                    edit_option = input('Invalid input, which profile field would you like to update (password, name, age, gender, location, preferred_genders): ')
                
                # get existing state of user's information
                info = user.get_user_info(user_id)
                
                # get the new information for the particular field
                if edit_option == 'password':
                    new_password = get_password()
                    info.password = new_password
                elif edit_option == 'username':
                    new_username = get_username()
                    info.username = new_username
                elif edit_option == 'name':
                    new_name = get_user_name()
                    info.name = new_name
                elif edit_option == 'age':
                    new_age = get_user_age()
                    info.age = new_age
                elif edit_option == 'gender':
                    new_gender = get_user_gender()
                    info.gender = new_gender
                elif edit_option == 'location':
                    new_location = get_user_location()
                    info.location = new_location
                elif edit_option == 'education':
                    new_education = get_user_education_level()
                    info.education = new_education
                elif edit_option == 'preferred_genders':
                    new_pref_genders = get_preferred_genders()
                    info.preferred_genders = new_pref_genders
                elif edit_option == 'preferred_age':
                    new_age_min, new_age_max = get_age_range()
                    info.age_low = new_age_min
                    info.age_high = new_age_max
                elif edit_option == 'interests':
                    new_interests = get_user_interests()
                    info.interests = new_interests
                elif edit_option == 'politics':
                    new_politics = get_political_view()
                    info.politics = new_politics
                elif edit_option == 'intentions':
                    new_intentions = get_dating_intentions()
                    info.intentions = new_intentions
                elif edit_option == 'weights':
                    new_weights = get_user_feature_weights()
                    info.weights = new_weights
                
                # update the user's info in the database
                user.update_user_info(info)

            elif option == 'view_all_profiles':
                print(user.get_all_users()[COLUMNS_TO_SHOW])

            else:
                print('Not a valid entry, please try again.')