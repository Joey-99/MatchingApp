import random
from user_management_new import user_management_new  

# Instantiate the user management object
user_management = user_management_new()

# Function to generate random user data
def generate_random_user_data():
    names = [
        "John", "Alice", "Bob", "Diana", "Edward", "Fiona", "George", "Hannah", "Ian", "Julia",
        "Kevin", "Laura", "Michael", "Nina", "Oscar", "Paula", "Quentin", "Rachel", "Steven", "Tina",
        "Uma", "Victor", "Wendy", "Xander", "Yvonne", "Zack", "Chris", "Angela", "Dennis", "Ellie",
        "Frank", "Gina", "Henry", "Isla", "Jack", "Kara", "Leo", "Mona", "Nick", "Olivia", "Peter",
        "Queen", "Roger", "Sophia", "Tom", "Ursula", "Vince", "Wally", "Xena", "Yara", "Zane"
    ]
    
    locations = [
        "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio",
        "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "Charlotte",
        "San Francisco", "Indianapolis", "Seattle", "Denver", "Washington D.C.", "Miami", "Atlanta", "Boston"
    ]
    
    genders = ['M', 'F', 'O']
    preferred_genders_options = ['M', 'F', 'O', 'MF', 'MFO', 'FO']

    username = "user" + str(random.randint(1000, 9999))
    password = "pass" + str(random.randint(1000, 9999))
    name = random.choice(names)
    age = random.randint(18, 70)
    gender = random.choice(genders)
    location = random.choice(locations)
    preferred_genders = random.choice(preferred_genders_options)
    age_low = random.randint(18, age)  # Ensure age_low is less than or equal to user's age
    age_high = random.randint(age, 70)  # Ensure age_high is greater than or equal to user's age

    return username, password, name, age, gender, location, preferred_genders, age_low, age_high

# Creating 200 user profiles
created_count = 0
for i in range(200):
    username, password, name, age, gender, location, preferred_genders, age_low, age_high = generate_random_user_data()
    
    # Ensure the username is unique
    if not user_management.check_valid_username(username):
        print(f"Skipping duplicate username: {username}")
        continue

    user_profile = user_management.create_user(username, password, name, age, gender, location, [], preferred_genders, age_low, age_high)
    user_management.add_user_to_db(user_profile)
    
    created_count += 1
    print(f"Created user {i+1}: {username} - {name}, {age}, {gender}, {location}")

print(f"{created_count} user profiles have been successfully created for testing.")
