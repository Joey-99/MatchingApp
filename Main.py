from User import User

if __name__ == '__main__':
    # Instantiate the user object
    user = User()
    while True:
        # receive input commands
        cmd = input("Please enter the command: ")
        # exit commands
        if cmd == 'exit':
            print("bye~")
            break
        # create the user
        elif cmd == 'create_user':
            # name input
            name = input("Please enter the name: ")
            # age input
            age = input("Please enter the age (1-100): ")
            # check the age eligibility 
            while True:
                try:
                    age = int(age)
                    if age < 1 or age > 100:
                        raise ValueError
                    break
                except Exception:
                    age = input("age Error, Please enter the age(1-100): ")
            # gender input
            gender = input("Please enter the gender (1 for male, 2 for female): ")
            # check the gender eligibility
            while True:
                try:
                    gender = int(gender)
                    if gender != 1 and gender != 2:
                        raise ValueError
                    break
                except Exception:
                    gender = input("gender Error, Please enter the gender (1 for male, 2 for female): ")
            # location input
            location = input("Please enter the location: ")
            # query the current available user_id
            user_id = user.getUserIdUnique()
            # create the user
            success = user.create(
                user_id,
                name,
                age,
                gender,
                location,
                []
            )
            # check if the user created successfully
            if success:
                print("User created successfully")
            else:
                print("User created failure")
        # query all users
        elif cmd == 'view_profiles':

            # query all users
            users = user.getAll()

            # check if the users is null
            if users is []:
                print("No users")
            else:
                for line in users:
                    print(line)
        # edit user profile
        elif cmd == 'edit_profile':
            # get the user ID want to modify
            id = input("Please enter the user_id you want to modify (0 to exit): ")
            # check if the user ID is true
            while True:
                # check if want to exit
                if id == '0' or id == 0:
                    break
                # check if the input ID is true
                try:
                    id = int(id)
                    if user.findUserIdUnique(id) == False:
                        raise ValueError
                    break
                except Exception:
                    id = input("user_id is not find. Please enter the user_id (0 to exit): ")

            # check if want to exit
            if id == '0' or id == 0:
                continue

            # get the attributes want to modify
            key = input("Please enter the attribute(name, age, gender, location, interests): ")
            while True:
                # check attributes if true
                if key not in ['name', 'age', 'gender', 'location', 'interests']:
                    key = input("Attribute Error. Please enter the attribute (name, age, gender, location, interests): ")
                    continue
                else:
                    break
            # get the attributes want to modify
            value = None
            if key == 'name':
                value = input("Please enter the new name: ")
            elif key == 'age':
                # check if the age input is true
                value = input("Please enter the age (1-100): ")
                while True:
                    try:
                        value = int(value)
                        if value < 1 or value > 100:
                            raise ValueError
                        break
                    except Exception:
                        value = input("age Error, Please enter the age(1-100): ")
            elif key == 'gender':
                # check if the gender input is true
                value = input("Please enter the gender (1 for male, 2 for female): ")
                while True:
                    try:
                        value = int(value)
                        if value != 1 and value != 2:
                            raise ValueError
                        break
                    except Exception:
                        value = input("gender Error, Please enter the gender (1 for male, 2 for female): ")
            if key == 'location':
                value = input("Please enter the new location: ")
            # modify
            success = user.change(id, key, value)
            # check if the modify successfully
            if success:
                print("User change successfully")
            else:
                print("User change failure")
        # delete the user profile
        elif cmd == 'delete_profile':
            # get the user ID want to modify
            id = input("Please enter the user_id you want to delete (0 to exit): ")
            # check if the user ID is true
            while True:
                # check if want to exit
                if id == '0' or id == 0:
                    break
                # get the user ID want to modify
                try:
                    id = int(id)
                    if user.findUserIdUnique(id) == False:
                        raise ValueError
                    break
                except Exception:
                    id = input("user_id is not find. Please enter the user_id (0 to exit): ")
            # check if want to exit
            if id == '0' or id == 0:
                continue
            # delete
            success = user.delete(id)
            # check if delete is successfully
            if success:
                print("User deleted successfully")
            else:
                print("User deleted failure")
