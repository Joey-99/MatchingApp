import sqlite3
import os
import pandas as pd
from users import User

class user_management_new:
    def __init__(self):
        self.db_file = 'users.db'
        new_table = self.establish_tables()
        if new_table:
            self.curr_user_id = 0
        else:
            self.curr_user_id = self.get_curr_user_id()

    def get_curr_user_id(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute("""SELECT MAX(user_id) FROM users""")
        try:
            max_user_id = cursor.fetchone()[0] + 1
        except:
            max_user_id = 0
        return max_user_id

    def establish_tables(self):
        if os.path.exists(self.db_file):
            print('Database exists')
            return False
        else:
            self.create_user_table()
            self.create_like_dislike_table()
            print('Successfully created user database')
            return True

    def create_user_table(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                       user_id INTEGER PRIMARY KEY,
                       username TEXT KEY,
                       password TEXT KEY,
                       name TEXT KEY,
                       age INTEGER KEY,
                       gender TEXT KEY,
                       location TEXT KEY,
                       preferred_genders TEXT KEY,
                       age_limit INTEGER KEY)""")
        
        conn.commit()
        conn.close()

    def create_like_dislike_table(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS likes(
                       user_id INTEGER KEY,
                       liked_user_id INTEGER KEY)""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS dislikes(
                       user_id INTEGER KEY,
                       disliked_user_id INTEGER KEY)""")
        
        conn.commit()
        conn.close()

    def check_valid_username(self, username):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT * FROM users
                       WHERE username = '{username}'""")
        result = cursor.fetchall()
        conn.close()
        return True if len(result) == 0 else False
    
    def get_user_password(self, username):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT password FROM users
                       WHERE username = '{username}'""")
        password = cursor.fetchone()[0]
        return password

    def create_user(self, username, password, name, age, gender, location, interests, preferred_genders, age_limit):
        user = User(username, password, self.curr_user_id, name, age, gender, location, interests, preferred_genders, age_limit)
        self.curr_user_id += 1
        print('Successfull created new user')
        return user

    def add_user_to_db(self, user):
        print(user.username, user.password, user.user_id)
        valid = self.check_valid_username(user.username)
        
        if valid:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute(f"""INSERT INTO users(user_id,username,password,name,age,gender,location,preferred_genders,age_limit)
                           VALUES({user.user_id}, '{user.username}', '{user.password}', '{user.name}', '{user.age}',
                           '{user.gender}', '{user.location}', '{user.preferred_genders}', '{user.age_limit}')""")
            conn.commit()
            conn.close()
            print('Successfully added user to db')
            return True
        else:
            print('The username already exists')
            return False
        
    def delete_user_from_db(self, user_id):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM users WHERE user_id = {user_id}")
        conn.commit()
        conn.close()
        print('Successfully deleted user from db')
        return True
        
    def get_user_id(self, username):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT user_id FROM users
                       WHERE username = '{username}'""")
        user_id = cursor.fetchone()[0]
        return user_id
    
    def get_preferred_genders(self, user_id):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT preferred_genders FROM users
                       WHERE user_id = '{user_id}'""")
        preferred_genders = cursor.fetchone()[0]
        return list(preferred_genders)
    
    def get_age_limit(self, user_id):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT age_limit FROM users
                       WHERE user_id = '{user_id}'""")
        age_limit = cursor.fetchone()[0]
        return age_limit
    
    def get_liked_profiles(self, user_id):
        conn = sqlite3.connect(self.db_file)
        query = f"""SELECT * FROM likes
                       WHERE user_id = '{user_id}'"""
        liked_profiles = pd.read_sql_query(query, conn)
        conn.close()
        return liked_profiles['liked_user_id'].tolist()
    
    def get_admirers_profiles(self, user_id):
        conn = sqlite3.connect(self.db_file)
        query = f"""SELECT * FROM likes
                       WHERE liked_user_id = '{user_id}'"""
        liked_profiles = pd.read_sql_query(query, conn)
        conn.close()
        return liked_profiles['user_id'].tolist()
        
    def get_disliked_profiles(self, user_id):
        conn = sqlite3.connect(self.db_file)
        query = f"""SELECT * FROM dislikes
                       WHERE user_id = '{user_id}'"""
        disliked_profiles = pd.read_sql_query(query, conn)
        conn.close()
        return disliked_profiles['disliked_user_id'].tolist()

    def get_all_users(self):
        conn = sqlite3.connect(self.db_file)
        query = f"""SELECT * FROM users"""
        users = pd.read_sql_query(query, conn)
        conn.close()
        return users

    def get_interests(self, user_id):
        preferred_genders = self.get_preferred_genders(user_id)
        liked_profiles = self.get_liked_profiles(user_id)
        disliked_profiles = self.get_disliked_profiles(user_id)

        all_users = self.get_all_users()
        all_users = all_users[all_users['user_id'] != user_id]
        gender_filtered = all_users[all_users['gender'].isin(preferred_genders)]
        seen_filtered = gender_filtered[~gender_filtered['user_id'].isin(liked_profiles + disliked_profiles)]
        return seen_filtered
    
    def like_profile(self, user_id, other_user_id):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO likes(user_id,liked_user_id)
                        VALUES({user_id}, {other_user_id})""")
        conn.commit()
        conn.close()
        return True
    
    def dislike_profile(self, user_id, other_user_id):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO dislikes(user_id,disliked_user_id)
                        VALUES({user_id}, {other_user_id})""")
        conn.commit()
        conn.close()
        return True
    
    def evaluate_matches(self, user_id):
        liked = self.get_liked_profiles(user_id)
        admirers = self.get_admirers_profiles(user_id)
        mutual = set(liked).intersection(set(admirers))
        all_users = self.get_all_users()
        mutual_profiles = all_users[all_users['user_id'].isin(mutual)]
        return mutual_profiles
    
    def update_field(self, user_id, column_name, column_value):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute(f"""UPDATE users
                       SET {column_name} = '{column_value}'
                       WHERE user_id = {user_id}""")
        conn.commit()
        conn.close()
        return True

if __name__ == "__main__":
    user = user_management_new()
    user_id = user.get_user_id('armaan2')
    print(user_id)
    matches = user.evaluate_matches(user_id)
    print(matches)