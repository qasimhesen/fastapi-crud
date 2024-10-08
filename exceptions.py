from fastapi import HTTPException , status

class DetailedHTTPException(HTTPException):
    STATUS_CODE = 404
    DETAIL = "server error"


    def __init__(self):
        super().__init__(status_code = self.STATUS_CODE , detail = self.DETAIL)



class UserNotFoundException(DetailedHTTPException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "user is not found"
    