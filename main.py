from database import connection
from models import User
user = User('Robert.Kowalski', 'robert.kowalski@gmail.com', 'tajne123')


def show_users(cursor):
    users = User.load_all(cursor)
    for user in users:
        print(user.id, user.username, user.hashed_password, user.email)

cnx = connection('pyt_s_16_warsztat_2')
cursor = cnx.cursor()
#user.save(cursor)
user_id = 3
user = User.load_by_id(cursor, user_id)
if user is not None:
    print(user.username, user.hashed_password, user.email)

    print(user.id)
else:
    print("Nie ma użytkownika o id = ", user_id)

show_users(cursor)

user2 = User.load_by_id(cursor, 5)
user2.username='Roman.Kowalski'
user2.save(cursor)
print('Po zmianie')


show_users(cursor)
print()
user2.delete(cursor)
show_users(cursor)
cursor.close()
cnx.close()