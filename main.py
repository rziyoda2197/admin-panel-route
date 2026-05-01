from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

app = FastAPI()

# Basic Auth credentials
basic_auth = HTTPBasic()

class User(BaseModel):
    username: str
    password: str

# Basic Auth funksiyasi
def basic_auth_check(credentials: HTTPBasicCredentials = Depends(basic_auth)):
    if credentials.username == "admin" and credentials.password == "password":
        return credentials
    raise HTTPException(status_code=401, detail="Invalid username or password")

@app.get("/admin-panel")
async def admin_panel(credentials: HTTPBasicCredentials = Depends(basic_auth_check)):
    return {"message": "Welcome to admin panel"}
```

Kodni ishga tushirish uchun FastAPI serveri ishga tushirish va `http://localhost:8000/admin-panel` ga kirish uchun `admin` va `password` ni kiritish kerak.
