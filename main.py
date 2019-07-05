from database import connection
from models import User
user = User('Adam.Nowak', 'adam.nowak@gmail.com', 'tajne123')

print(user.username, user.hashed_password, user.email)

cnx = connection('pyt_s_16_warsztat_2')
cursor = cnx.cursor()
user.save(cursor)
print(user.id)
cursor.close()
cnx.close()