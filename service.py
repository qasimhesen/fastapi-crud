from models import User
from schema import UserCreateSchema , UserDeleteSchema, UserGetSchema, UserUpdateSchema
from sqlalchemy.orm import Session
from exceptions import UserNotFoundException

def create_user_in_db(*, data: UserCreateSchema, db : Session):
    new_user = User(username = data.username , password = data.password)
    user = db.query(User).filter_by(username=data.username).first()

    if user:
        raise UserNotFoundException()
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg" : "new user is created"}


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
    user = db.query(User).filter_by(username=user_name,password=data.password).first()
    if not user:
        raise UserNotFoundException()
    
    db.query(User).filter_by(username=user_name,password=data.password).update({"password":data.new_password})
    db.commit()
    db.refresh(user)

    return {"msg": "user is updated"}