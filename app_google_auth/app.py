import httpx
from fastapi import FastAPI, HTTPException, Security, status, Depends
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel

# See https://developers.google.com/identity/protocols/oauth2/openid-connect#obtaininguserprofileinformation
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"


class User(BaseModel):
    id: str
    email: str
    domain: str


async def authenticate(
    oauth_token: str = Security(APIKeyHeader(name="Authorization")),
) -> User:
    """Decodes Google Apps Script's ScriptApp.getOAuthToken()
    and returns a User object if successful, otherwise raises 401
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(GOOGLE_DISCOVERY_URL)
        userinfo_url = response.json()["userinfo_endpoint"]  # Could be cached
        response = await client.get(
            userinfo_url, headers={"Authorization": f"Bearer {oauth_token}"}
        )
    if response.status_code == 200:
        userinfo = response.json()
        user = User(
            id=userinfo["sub"], email=userinfo["email"], domain=userinfo.get("hd")
        )
        if True:
            # TODO: authenticate the user here or as part of the User model
            # E.g. to allow all users from a certain domain:
            # if user.domain == 'mydomain.com'
            return user
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Unauthorized",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid OAuth Token",
        )


async def get_current_user(user: User = Depends(authenticate)) -> User:
    return user


# Require authentication for every endpoint
app = FastAPI(dependencies=[Security(authenticate)])
