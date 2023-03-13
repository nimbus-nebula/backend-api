from fastapi import APIRouter
from starlette.requests import Request
from fastapi_sso.sso.google import GoogleSSO

router = APIRouter()
google_sso = GoogleSSO("my-client-id",
                       "my-client-secret",
                       "https://my.awesome-web.come/google/callback")


@router.get("/api/auth/google/login")
async def google_login():
    """Generate login url and redirect"""
    return await google_sso.get_login_redirect()


@router.get("/api/auth/google/callback")
async def google_callback(request: Request):
    """Handle callback and get user info"""
    user = await google_sso.verify_and_process(request)
    return {
        "id": user.id,
        "picture": user.picture,
        "display_name": user.display_name,
        "email": user.email,
        "provider": user.provider,
    }
