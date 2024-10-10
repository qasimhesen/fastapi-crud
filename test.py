import bcrypt

user_password="salam"
new_password="salam2"



a=bcrypt.checkpw(user_password.encode('utf-8'), new_password.encode('utf-8'))
print(a)
