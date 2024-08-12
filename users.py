class User:
    def __init__(self, username, password, user_id, name, age, gender, location, interests,
                 liked_users=[], disliked_users=[], matches=[]):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.interests = interests
        self.liked_users = liked_users
        self.disliked_users = disliked_users
        self.matches = matches
    
    def like(self, other_user):
        if other_user.user_id not in self.liked_users:
            self.liked_users.append(other_user.user_id)
        if self.user_id in other_user.liked_users and other_user.user_id not in self.matches:
            self.matches.append(other_user.user_id)
            other_user.matches.append(self.user_id)

    def dislike(self, other_user):
        if other_user.user_id not in self.disliked_users:
            self.disliked_users.append(other_user.user_id)