from models import User
from schema import UserCreateSchema , UserDeleteSchema, UserGetSchema, UserUpdateSchema
from sqlalchemy.orm import Session
from exceptions import UserNotFoundException , UserIsAlreadyExistException , IsNotCorrectException

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
    hashed_password = bcrypt.hashpw(data.new_password.encode('utf-8'), bcrypt.gensalt())
    
    if not user:
        raise UserNotFoundException()
    

    
    hashed_password_input = bcrypt.hashpw(data.password.encode('utf-8'), bcrypt.gensalt())

    db.query(User).filter_by(username=user_name,password=hashed_password_input).update({"password":hashed_password})
    
    #new push
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