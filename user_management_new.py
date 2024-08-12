import sqlite3
import os
from users import User

class user_management_new:
    def __init__(self):
        self.db_file = 'users.db'
        new_table = self.establish_table()
        if new_table:
            self.curr_user_id = 0
        else:
            self.curr_user_id = self.get_curr_user_id()

    def get_curr_user_id(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute("""SELECT MAX(user_id) FROM users""")
        max_user_id = cursor.fetchone()[0]
        return max_user_id + 1

    def establish_table(self):
        if os.path.exists(self.db_file):
            print('Table exists')
            return False
        else:
            self.create_table()
            print('Successfully created table')
            return True

    def create_table(self):
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                       user_id INTEGER PRIMARY KEY,
                       username TEXT KEY,
                       password TEXT KEY,
                       name TEXT KEY,
                       age INTEGER KEY,
                       gender TEXT KEY,
                       location TEXT KEY)""")
        
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

    def create_user(self, username, password, name, age, gender, location, interests,
                 liked_users=[], disliked_users=[], matches=[]):
        user = User(username, password, self.curr_user_id, name, age, gender, location, interests,
                    liked_users, disliked_users, matches)
        self.curr_user_id += 1
        print('Successfull created new user')
        return user

    def add_user_to_db(self, user):
        print(user.username, user.password, user.user_id)
        valid = self.check_valid_username(user.username)
        
        if valid:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            cursor.execute(f"""INSERT INTO users(user_id,username,password,name,age,gender,location)
                           VALUES({user.user_id}, '{user.username}', '{user.password}', '{user.name}', '{user.age}',
                           '{user.gender}', '{user.location}')""")
            conn.commit()
            conn.close()
            print('Successfully added user to db')
            return True
        else:
            print('The username already exists')
            return False