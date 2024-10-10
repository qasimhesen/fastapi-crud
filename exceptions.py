from fastapi import HTTPException , status

class DetailedHTTPException(HTTPException):
    STATUS_CODE = 404
    DETAIL = "server error"


    def __init__(self):
        super().__init__(status_code = self.STATUS_CODE , detail = self.DETAIL)

class DetailHTTPException1(HTTPException):
    STATUS_CODE = 406
    DETAIL = "server error"

    def __init__(self):
        super().__init__(status_code = self.STATUS_CODE , detail = self.DETAIL)


class DetailHTTPException2(HTTPException):
    STATUS_CODE = 400
    DETAIL = "server error"

    def __init__(self):
        super().__init__(status_code = self.STATUS_CODE , detail = self.DETAIL)




class UserNotFoundException(DetailedHTTPException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "user is not found"


class UserIsAlreadyExistException(DetailHTTPException1):
    STATUS_CODE = status.HTTP_406_NOT_ACCEPTABLE
    DETAIL = "user is already exist"
    

class IsNotCorrectException(DetailHTTPException2):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "password is not correct"