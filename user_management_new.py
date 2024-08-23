import sqlite3
import os
import pandas as pd
import numpy as np
from users import User
from matching_helpers import *

class user_management_new:
    def __init__(self):
        '''
        Initialization function
        Establishes the database and the three tables
        Calculates the next user_id to be used for a new user
        '''
        self.db_file = 'users.db'
        new_table = self.establish_tables()
        # sets the user id depending on if it is a new/existing db
        if new_table:
            self.curr_user_id = 0
        else:
            self.curr_user_id = self.get_curr_user_id()

    def get_curr_user_id(self):
        '''
        Gets the current highest user_id in use
        Returns 0 if no user's are created
        '''
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute("""SELECT MAX(user_id) FROM users""")
        try:
            max_user_id = cursor.fetchone()[0] + 1
        except:
            max_user_id = 0
        return max_user_id

    def establish_tables(self):
        '''
        Creates the users, likes, and dislikes tables
        '''
        if os.path.exists(self.db_file):
            print('Database exists')
            return False
        else:
            self.create_user_table()
            self.create_like_dislike_table()
            print('Successfully created user database')
            return True

    def create_user_table(self):
        '''
        Creates the primary user table
        '''
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # creates the user table with all the necessary fields
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                       user_id INTEGER PRIMARY KEY,
                       username TEXT KEY,
                       password TEXT KEY,
                       name TEXT KEY,
                       age INTEGER KEY,
                       gender TEXT KEY,
                       location TEXT KEY,
                       education TEXT KEY,
                       interests TEXT KEY,
                       politics TEXT KEY,
                       intentions TEXT KEY,
                       preferred_genders TEXT KEY,
                       age_low INTEGER KEY,
                       age_high INTEGER KEY,
                       weights TEXT KEY)""")
        
        conn.commit()
        conn.close()

    def create_like_dislike_table(self):
        '''
        Creates the two tables that keep track of likes/dislikes
        '''
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        # creates the likes and dislikes tables with all the necessary fields
        cursor.execute("""CREATE TABLE IF NOT EXISTS likes(
                       user_id INTEGER KEY,
                       liked_user_id INTEGER KEY)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS dislikes(
                       user_id INTEGER KEY,
                       disliked_user_id INTEGER KEY)""")
        
        conn.commit()
        conn.close()

    def check_valid_username(self, username):
        '''
        Checks if a username is already in the database
        Used when a new user is creating a profile
        '''
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT * FROM users
                       WHERE username = '{username}'""")
        result = cursor.fetchall()
        conn.close()
        return True if len(result) == 0 else False
    
    def get_user_password(self, username):
        '''
        Gets the associated password for a specific username
        '''
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT password FROM users
                       WHERE username = '{username}'""")
        password = cursor.fetchone()[0]
        return password

    def create_user(self, username, password, name, age, gender, location, education, interests, politics, intentions,
                    preferred_genders, age_low, age_high, weights):
        '''
        Creates an instance of the user class
        Increments the current user id variable
        '''
        user = User(username, password, self.curr_user_id, name, age, gender, location, education, interests, politics, intentions,
                    preferred_genders, age_low, age_high, weights)
        self.curr_user_id += 1
        print('Successfull created new user')
        return user

    def add_user_to_db(self, user):
        '''
        Adds a new user to the database
        Ensures a valid username
        Populates all the columns in the new row
        '''
        valid = self.check_valid_username(user.username)
        # processes the interests/weights as strings in order to populate into the table
        interests_string = ','.join(user.interests)
        weights_string = ','.join(map(str, user.weights))
        
        if valid:
            # adds the user information as a new entry in the user's table
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute(f"""INSERT INTO users(user_id,username,password,name,age,gender,location,education,interests,politics,intentions,preferred_genders,age_low,age_high,weights)
                           VALUES({user.user_id}, '{user.username}', '{user.password}', '{user.name}', {user.age},
                           '{user.gender}', '{user.location}', '{user.education}', '{interests_string}', '{user.politics}', '{user.intentions}',
                           '{user.preferred_genders}', {user.age_low}, {user.age_high}, '{weights_string}')""")
            conn.commit()
            conn.close()
            print('Successfully added user to db')
            return True
        else:
            print('The username already exists')
            return False
        
    def delete_user_from_db(self, user_id):
        '''
        Removes a user from the database
        Removes from user table and any entries in the likes/dislikes that contains their user id
        '''
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        # deletes the user from the user table, and any entries in likes/dislikes that contains their user_id
        cursor.execute(f"DELETE FROM users WHERE user_id = {user_id}")
        cursor.execute(f"DELETE FROM likes WHERE user_id = {user_id} OR liked_user_id == {user_id}")
        cursor.execute(f"DELETE FROM dislikes WHERE user_id = {user_id} OR disliked_user_id == {user_id}")
        conn.commit()
        conn.close()
        print('Successfully deleted user from db')
        return True
        
    def get_user_id(self, username):
        '''
        Gets the user_id associated with a username
        '''
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT user_id FROM users
                       WHERE username = '{username}'""")
        user_id = cursor.fetchone()[0]
        conn.close()
        return user_id
    
    def get_preferred_genders(self, user_id):
        '''
        Gets the preferred genders of an associated user_id
        '''
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT preferred_genders FROM users
                       WHERE user_id = {user_id}""")
        preferred_genders = cursor.fetchone()[0]
        conn.close()
        return list(preferred_genders)
    
    def get_liked_profiles(self, user_id):
        '''
        Gets all profiles the user has liked
        '''
        conn = sqlite3.connect(self.db_file)
        query = f"""SELECT * FROM likes
                       WHERE user_id = {user_id}"""
        liked_profiles = pd.read_sql_query(query, conn)
        conn.close()
        return liked_profiles['liked_user_id'].tolist()
    
    def get_admirers_profiles(self, user_id):
        '''
        Gets all profiles that have liked a user
        '''
        conn = sqlite3.connect(self.db_file)
        query = f"""SELECT * FROM likes
                       WHERE liked_user_id = {user_id}"""
        liked_profiles = pd.read_sql_query(query, conn)
        conn.close()
        return liked_profiles['user_id'].tolist()
        
    def get_disliked_profiles(self, user_id):
        '''
        Gets all profiles a user has disliked
        '''
        conn = sqlite3.connect(self.db_file)
        query = f"""SELECT * FROM dislikes
                       WHERE user_id = {user_id}"""
        disliked_profiles = pd.read_sql_query(query, conn)
        conn.close()
        return disliked_profiles['disliked_user_id'].tolist()

    def get_all_users(self):
        '''
        Gets all created users
        '''
        conn = sqlite3.connect(self.db_file)
        query = f"""SELECT * FROM users"""
        users = pd.read_sql_query(query, conn)
        conn.close()
        return users

    def get_user_info(self, user_id):
        '''
        Gets all attributes of a particular user
        '''
        conn = sqlite3.connect(self.db_file)
        query = f"""SELECT * FROM users
                WHERE user_id = {user_id}
                """
        u = pd.read_sql_query(query, conn)
        # processes the interests/weights back into lists
        u['interests'] = u['interests'].apply(lambda x: x.split(',') if x else [])
        u['weights'] = u['weights'].apply(lambda x: list(map(int, x.split(','))) if x else [])
        # creates a user object
        user = User(u.iloc[0].username, u.iloc[0].password, u.iloc[0].user_id, u.iloc[0]['name'], u.iloc[0].age, u.iloc[0].gender,
                    u.iloc[0].location, u.iloc[0].education, u.iloc[0].interests, u.iloc[0].politics, u.iloc[0].intentions,
                    u.iloc[0].preferred_genders, u.iloc[0].age_low, u.iloc[0].age_high, u.iloc[0].weights)
        conn.close()
        return user

    def update_user_info(self, user):
        '''
        Updates an existing user with any new information that has been provided
        '''
        # processes the interests/weights lists into strings
        interests_string = (','.join(list(user.interests)))
        weights_string = ','.join(list(map(str, user.weights)))
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        # updates the user's entry with new information
        cursor.execute(f"""UPDATE users
                        SET username = '{user.username}', 
                            password = '{user.password}', 
                            name = '{user.name}', 
                            age = {user.age}, 
                            gender = '{user.gender}', 
                            location = '{user.location}', 
                            education = '{user.education}', 
                            interests = '{interests_string}', 
                            politics = '{user.politics}', 
                            intentions = '{user.intentions}', 
                            preferred_genders = '{user.preferred_genders}', 
                            age_low = {user.age_low}, 
                            age_high = {user.age_high},
                            weights = '{weights_string}'
                        WHERE user_id = {user.user_id}""")
        conn.commit()
        conn.close()
        print(f'Successfully updated user {user.user_id} in db')
        return True

    def get_potentials(self, user_id):
        '''
        Gets all profiles that a user has not seen
        Also ensures the profiles being shown matches the user's preferences
        '''
        # gets the user's preferred genders, and any likes/dislikes/liked us
        preferred_genders = self.get_preferred_genders(user_id)
        liked_profiles = self.get_liked_profiles(user_id)
        disliked_profiles = self.get_disliked_profiles(user_id)
        liked_us = self.get_admirers_profiles(user_id)

        all_users = self.get_all_users().copy()
        all_users['interests'] = all_users['interests'].apply(lambda x: x.split(',') if x else [])
        all_users['weights'] = all_users['weights'].apply(lambda x: list(map(int, x.split(','))) if x else [])
        # gets relevant other user's in order to rank
        actual_user = all_users[all_users['user_id'] == user_id]
        all_users = all_users[all_users['user_id'] != user_id]

        # gets any necessary user features necessary to rank other user's
        age_low = int(actual_user['age_low'].values[0])
        age_high = int(actual_user['age_high'].values[0])
        interests = set(actual_user['interests'].values[0])
        location = actual_user['location'].values[0]
        education = actual_user['education'].values[0]
        politics = actual_user['politics'].values[0]
        intention = actual_user['intentions'].values[0]
        weights = np.array(actual_user['weights'].values[0])
        
        # remove any user's not in the preferred genders of the current user
        gender_filtered = all_users[all_users['gender'].isin(preferred_genders)]
        # remove any user's the current user has already liked/disliked
        seen_filtered = gender_filtered[~gender_filtered['user_id'].isin(liked_profiles + disliked_profiles)]

        # calculates the associated score of each feature
        seen_filtered['age_score'] = seen_filtered['age'].apply(lambda x: get_age_score(x, age_low, age_high))
        seen_filtered['interest_score'] = seen_filtered['interests'].apply(lambda x: get_interests_score(x, interests))
        seen_filtered['location_score'] = seen_filtered['location'].apply(lambda x: get_location_score(x,location))
        seen_filtered['education_score'] = np.where(seen_filtered['education'] == education, 1, 0)
        seen_filtered['politics_score'] = np.where(seen_filtered['politics'] == politics, 1, 0)
        seen_filtered['intention_score'] = np.where(seen_filtered['intentions'] == intention, 1, 0)
        seen_filtered['liked_user'] = np.where(seen_filtered['user_id'].isin(liked_us), 1, 0)

        # multiplies the user's scores by the normalized weight vector
        all_scores = seen_filtered[['age_score', 'interest_score', 'location_score', 'education_score', 'politics_score', 'intention_score', 'liked_user']]
        all_scores = np.array(all_scores)
        weighted_score = all_scores @ (weights / np.sum(weights))
        seen_filtered['weighted_score'] = weighted_score
        # sort the user's potentials in order by their compatability score (highes to lowest)
        seen_filtered = seen_filtered.sort_values(by='weighted_score', ascending=False)

        return seen_filtered
    
    def like_profile(self, user_id, other_user_id):
        '''
        Populates the like table with a user_id and the user_id they have liked
        '''
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO likes(user_id,liked_user_id)
                        VALUES({user_id}, {other_user_id})""")
        conn.commit()
        conn.close()
        return True
    
    def dislike_profile(self, user_id, other_user_id):
        '''
        Populates the dislike table with a user_id and the user_id they have disliked
        '''
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO dislikes(user_id,disliked_user_id)
                        VALUES({user_id}, {other_user_id})""")
        conn.commit()
        conn.close()
        return True
    
    def evaluate_matches(self, user_id):
        '''
        Function that finds all matches for an associated user_id
        '''
        liked = self.get_liked_profiles(user_id)
        admirers = self.get_admirers_profiles(user_id)
        mutual = set(liked).intersection(set(admirers))
        all_users = self.get_all_users()
        mutual_profiles = all_users[all_users['user_id'].isin(mutual)]
        return mutual_profiles
    
    def number_of_matches(self, user_id):
        '''
        Function that returns the total number of matches for a user
        '''
        return len(self.evaluate_matches(user_id))