from fastapi import Request, HTTPException, status, Depends
from app.utils import verify_token

def get_token_from_cookies(request: Request) -> str:
    token = request.cookies.get("token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )
    return token

def get_current_user(request: Request) -> dict:
    token = get_token_from_cookies(request)
    payload = verify_token(token)
    return payload  # Contains fields like "sub", "role", etc.

def get_current_admin_user(
    current_user: dict = Depends(get_current_user)
) -> dict:
    if current_user.get("role") != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admins only",
        )
    return current_user
