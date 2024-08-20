class User:
    def __init__(self, username, password, user_id, name, age, gender, location,education, interests, politics, intentions,
                 preferred_genders, age_low, age_high, weights):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.education = education
        self.interests = interests
        self.politics = politics
        self.intentions = intentions
        self.preferred_genders = preferred_genders
        self.age_low = age_low
        self.age_high = age_high
        self.weights = weights