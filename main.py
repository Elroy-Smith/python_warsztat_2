from models import User
user = User('Jan.Kowalski', 'jan.kowalski@gmail.com', 'tajne123')

print(user.username, user.hashed_password, user.email)