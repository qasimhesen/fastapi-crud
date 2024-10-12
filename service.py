#en axirinci kod budur
from models import User
from schema import UserCreateSchema , UserDeleteSchema, UserGetSchema, UserUpdateSchema, Reset_All_Base
from sqlalchemy.orm import Session
from exceptions import UserNotFoundException , UserIsAlreadyExistException , IsNotCorrectException
import psycopg2
from settings import DATABASE_URL

import bcrypt

def create_user_in_db(*, data: UserCreateSchema, db: Session):
    hashed_password = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt())
    new_user = User(username=data.username, password=hashed_password.decode('utf-8'))
    user = db.query(User).filter_by(username=data.username).first()

    if user:
        raise UserIsAlreadyExistException()
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": "new user is created"}



def delete_user_in_db(* , data: UserDeleteSchema, db : Session):
    user = db.query(User).filter_by(username=data.username).first()

    if not user:
        raise UserNotFoundException()
      
    db.delete(user)
    db.commit()
    return {"msg": "user is deleted"}


def get_user_by_username(*, username: str, db : Session):
    user = db.query(User).filter_by(username=username).first()

    if not user:
        raise UserNotFoundException()
    
    return UserGetSchema(username=user.username)





def change_user_password(user_name:str,data:UserUpdateSchema,db:Session):
    user = db.query(User).filter_by(username=user_name).first()
    hashed_password_new = bcrypt.hashpw(data.new_password.encode('utf-8'), bcrypt.gensalt())
    
    if not user:
        raise UserNotFoundException()
    
    if not bcrypt.checkpw(data.password.encode('utf-8'), user.password.encode('utf-8')):
        raise IsNotCorrectException()

    

    db.query(User).filter_by(username=user_name).update({"password":hashed_password_new.decode('utf-8')})
    
    db.commit()
    db.refresh(user)
    
    return {"msg": "user is updated"}



def check_password_in_db(user_name: str, user_password: str, db : Session):
    user = db.query(User).filter_by(username=user_name).first()

    if not user:
        raise UserNotFoundException()

    if not bcrypt.checkpw(user_password.encode('utf-8'), user.password.encode('utf-8')):
        raise IsNotCorrectException()
    return {"msg": "Password is correct"}


def reset_base(data:Reset_All_Base,db:Session):
    user = db.query(User).filter_by(username=data.username).first()
    if not user:
        raise UserNotFoundException()
    if not bcrypt.checkpw(password=data.password.encode("utf-8"),hashed_password=user.password.encode("utf-8")):
        raise UserNotFoundException

    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("DELETE FROM users;")

    cur.execute("ALTER SEQUENCE users_id_seq RESTART WITH 1;")
    conn.commit()
    cur.close()
    conn.close()
    return {"msg":"all user is deleted"}