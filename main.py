from database import connection
from models import User
user = User('Adam.Nowak1', 'adam.nowak@gmail.com', 'tajne123')


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
cursor.close()
cnx.close()