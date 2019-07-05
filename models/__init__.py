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

    def save(self, cursor):
        sql = """
        INSERT INTO "user"(username, email, hashed_password)
        VALUES (%s, %s, %s) RETURNING id
        """

        cursor.execute(sql, (self.username, self.email, self.hashed_password))

        last_id = cursor.fetchone()[0]
        self.__id = last_id

    @staticmethod
    def load_by_id(cursor, user_id):
        sql = """
        SELECT * FROM "user" WHERE id=%s
        """
        cursor.execute(sql, (user_id, ))
        data = cursor.fetchone()
        if data:
            id, username, email, hashed_password = data
            user = User(username, email, hashed_password)
            user._User__id = id
            return user
        else:
            return None