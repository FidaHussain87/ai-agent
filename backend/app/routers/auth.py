from fastapi import APIRouter, Depends, HTTPException, Response, status,Request
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from app.schemas.user import UserCreate, UserOut
from app.models.user import User
from app.database import SessionLocal
from app.utils.security import get_password_hash, verify_password, create_access_token,verify_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered.")
    hashed_password = get_password_hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password, role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login")
def login(response:Response,form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials.")
    access_token = create_access_token(data={"sub": user.email, "role": user.role})
    
    # Secure cookie set here
    response.set_cookie(
        key="token",
        value=access_token,
        httponly=True,
        secure=True,  # enable only if using HTTPS
        samesite="Lax",  # or "Strict" / "None"
        max_age=3600,
        path="/"
    )
    
    return {"message": "Login successful"}

@router.post("/logout")
def logout(response: Response):
    response = JSONResponse(content={"message": "Logged out"})
    response.delete_cookie("token")
    return response

@router.post("/refresh")
def refresh_token(request: Request, response: Response):
    token = request.cookies.get("token")
    if not token:
        raise HTTPException(status_code=401, detail="No token found")

    payload = verify_token(token)
    new_token = create_access_token(data={"sub": payload["sub"]})

    response.set_cookie(
        key="token",
        value=new_token,
        httponly=True,
        secure=True,
        samesite="Lax",
        max_age=3600,
        path="/"
    )

    return {"message": "Token refreshed"}
