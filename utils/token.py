from datetime import datetime,timedelta
from jose import JWTError,jwt
from schemas import schemas

SECRET_KEY="vsfgsd552knjkhlkkj245lkhjlghlglhghglhghggelellemdkf"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

def create_access_toekn(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username:str=payload.get("sub")
        if username  is None:
            raise credentials_exception
        token_data=schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception