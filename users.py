class User:
    def __init__(self, username, password, user_id, name, age, gender, location, interests, preferred_genders, age_limit):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.interests = interests
        self.preferred_genders = preferred_genders
        self.age_limit = age_limit