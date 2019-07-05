from crypto import password_hash, check_password

class User:
    def __init__(self, username, email, password):
        self.__id = - 1
        self.username = username
        self.email = email
        self.hashed_password = password

    @property
    def id(self):
        return self.__id

    @property
    def hashed_password(self):
        return self.__hashed_password

    @hashed_password.setter
    def hashed_password(self, password):
        self.__hashed_password = password_hash(password)
