import copy
import json
import os


class user_management:

    def __init__(self):
        self._list = None
        self._store_path = 'user_store.json'

    """
    method used to load the user_store.json file stored in the hard drive.
    If file not exist, then initialise self._list to an array of length 0.
    """

    def _load(self):
        """
        check if self._list is null
        if null, need initialization
        """
        if self._list is None:
            self._list = []
            # check if file exist
            if os.path.exists(self._store_path):
                # open the file
                with open(self._store_path, 'r', encoding='utf-8') as file:
                    try:
                        # read the file
                        content = file.read()
                        # deserialize json content
                        self._list = json.loads(content)
                    except json.JSONDecodeError:
                        print(self._store_path + " file is not json")
        return self._list

    '''
    store self._list content to user_store.json file
    '''

    def _dump(self):
        with open(self._store_path, 'w', encoding='utf-8') as file:
            # serialize content to json format
            content = json.dumps(self._list)
            # write the file
            file.write(content)

    '''
    check if the userID is exit
    '''

    def findUserIdUnique(self, userId):
        # load self._list
        self._load()
        # traverse self._list
        for user in self._list:
            # check if the userID searched is same
            if user['user_id'] == userId:
                return True
        return False

    '''
    query if want to create user, what's the current userID value should be
    '''

    def getUserIdUnique(self):
        user_id = 0
        # load self._list
        self._load()
        # traverse self._list
        for user in self._list:
            # check the max user_id
            if user['user_id'] > user_id:
                user_id = user['user_id']
        # ++1
        user_id += 1
        return user_id

    '''
    create a user object
    '''

    def create(self, user_id, name, age, gender, location, interests):
        # check if user_id is exit
        if self.findUserIdUnique(user_id):
            return False
        user = {}
        user["user_id"] = user_id
        user["name"] = name
        user["age"] = age
        user["gender"] = gender
        user["location"] = location
        user["interests"] = interests
        # add user object to the list
        self._list.append(user)
        # save a copy to drive
        self._dump()
        return True

    '''
    modify user
    user_id: the userID want to modify
    key: the attributes want to modify
    value: the value want to modify
    '''

    def change(self, user_id, key, value):
        # load self._list
        self._load()
        # traverse self._list
        for user in self._list:
            # check the matched user_id
            if user['user_id'] == user_id:
                # check if key exit
                if key in user:
                    user[key] = value
                    # save copy to drive
                    self._dump()
                    return True
        return False

    '''
    query all users
    '''

    def getAll(self):
        self._load()
        # avoid affecting self._list
        return copy.deepcopy(self._list)

    '''
    delete user
    user_id: the userID to delete
    '''

    def delete(self, user_id):
        # load self._list
        self._load()
        # traverse self._list
        for user in self._list:
            # query matched user_id
            if user['user_id'] == user_id:
                # delete
                self._list.remove(user)
                # save copy to drive
                self._dump()
                return True
        return False
