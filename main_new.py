import GUI
from user_management_new import user_management_new

COLUMNS_TO_SHOW = ['name', 'age', 'gender', 'location', "interests"]

def get_username():
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
    name = input("\nPlease enter your name: ")
    return name

def get_user_age():
    age = input("\nPlease enter your age (1-100): ")
    while True:
        try:
            age = int(age)
            if age < 1 or age > 100:
                raise ValueError
            break
        except Exception:
            age = input("Age error, please enter your age (1-100): ")
    return age

def get_user_feature_weights():
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
    location = input("\nPlease enter your location: ")
    return location

def get_user_location():
    location = input("\nPlease enter your location one of your cities in Ontario, Canada: ").strip(",._ ").lower()
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
        location = input("Invalid education level, please enter your location: ").strip(",._ ").lower()
    return location

def get_user_education_level():
    education = input("\nPlease enter your education level as following ['highschool', 'bachelor', 'master', 'phd']: ").strip(",._ ").lower()
    while education not in ['highschool', 'bachelor', 'master', 'phd']:
        education = input("Invalid education level, please enter your education level as following ['highschool', 'bachelor', 'master', 'phd']: ").strip(",._ ").lower()
    return education

def get_preferred_genders():
    gender_interest = input("\nPlease enter which genders you are interested in (i.e. 'MF' for male and female, 'MFO' for all, and 'F' for just female): ").strip().upper()
    while not set(gender_interest).issubset({'M', 'F', 'O'}) or len(gender_interest) != len(set(gender_interest)):
        gender_interest = input("Invalid genders, please enter which genders you are interested in (i.e. 'MF' for male and female, 'MFO' for all, and 'F' for just female): ").strip().upper()
    return gender_interest

def get_age_range():
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
    like = input("\nPlease enter whether you like or dislike this person ('like' or 'dislike' or 'exit'): ").lower()
    while like != 'like' and like != 'dislike' and like != 'exit':
        like = input("Invalid entry, please enter whether you like or dislike this person ('like' or 'dislike' or 'exit'): ").lower()
    return like

def get_password():
    password = input("\nPlease enter a password (minimum length of 5 characters): ")
    while len(password) < 5:
        password = input("Password must be a minumum of 5 characters: ")
    return password

# def get_user_interests():
#     interests = input("\nPlease enter your interests, separated by commas (e.g., swimming, reading, walking, soccer): ")
#     interests_list = [interest.strip() for interest in interests.split(',')]

#     return interests_list

def get_user_interests():
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
        # receive input commands
        logged_in = False
        cmd = input("\nPlease enter the command (login OR create_account): ").lower()
        
        # exit commands
        if cmd == 'create_account':
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

            user1 = user.create_user(username, password, name, age, gender, location, education, interests, politics, intentions, preferred_genders, age_low, age_high, weights)
            user.add_user_to_db(user1)
            print(f'\nWelcome {username}! :) Please select an option from the list below to get started:')
            logged_in = True
        elif cmd == 'login':
            username = input("\nPlease enter your username: ")
            user_exists = not user.check_valid_username(username)
            while not user_exists:
                username = input(f"The username '{username}' does not exists, please try again: ")
                user_exists = not user.check_valid_username(username)
            actual_password = user.get_user_password(username)
            password = input("\nEnter your password: ")
            while password != actual_password:
                password = input("The password you entered is incorrect, please try again: ")
            print(f'\nWelcome back {username}! :) Please select an option from the list below to get started:')
            logged_in = True
        elif cmd == 'gui':
            GUI.start()
            continue
        else:
            print("Not a valid command, please try again.")
            continue

        user_id = user.get_user_id(username)

        while logged_in:
            option = input("\nPlease choose an option (browse_profiles OR view_matches OR edit_profile OR logout OR delete_profile): ").lower()
            if option == 'logout':
                logged_in = False
                break
            elif option == 'browse_profiles':
                interests = user.get_potentials(user_id)
                exit = False
                for other_user_id in interests['user_id'].tolist():
                    if exit:
                        break
                    print(interests[interests['user_id'] == other_user_id][COLUMNS_TO_SHOW])
                    like = get_like_dislike()
                    if like == 'exit':
                        exit = True
                        continue
                    elif like == 'like':
                        user.like_profile(user_id, other_user_id)
                    elif like == 'dislike':
                        user.dislike_profile(user_id, other_user_id)
                if not exit:
                    print('\nYou have viewed all profiles, please check again later for more.')
            elif option == 'view_matches':
                matches = user.evaluate_matches(user_id)
                if len(matches) == 0:
                    print('\nYou have no matches at this time, keep liking profiles :)')
                else:
                    print('\nYou have matched with the following users\n')
                    print(matches[COLUMNS_TO_SHOW])
            elif option == 'delete_profile':
                sure = input('\nAre you sure you want to delete your profile (Y/N): ').upper()
                while sure != 'Y' and sure != 'N':
                    sure = input('Invalid input, are you sure you want to delete your profile (Y/N): ').upper()
                if sure == 'Y':
                    user.delete_user_from_db(user_id)
                    success_delete = user.check_valid_username(username)
                    print('We are sad to see you go :(')
                    if success_delete:
                        logged_in = False
                        break
                    else:
                        continue
                elif sure == 'N':
                    continue
            elif option == 'edit_profile':
                edit_option = input('\nWhich profile field would you like to update (username, password, name, age, gender, location, education, politics, intentions, interests, preferred_genders, preferred_age, weights): ')
                while edit_option not in ['username', 'password', 'name', 'age', 'gender', 'location', 'education', 'preferred_genders', 'preferred_age', 'interests', 'politics', 'intentions', 'weights']:
                    edit_option = input('Invalid input, which profile field would you like to update (password, name, age, gender, location, preferred_genders): ')
                info = user.get_user_info(user_id)
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
                user.update_user_info(info)
