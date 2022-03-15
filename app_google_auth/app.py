import httpx
from fastapi import FastAPI, HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel

GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"


class User(BaseModel):
    id: str
    email: str


async def decode_oauth_token(
    oauth_token: str = Security(APIKeyHeader(name="Authorization")),
) -> User:
    """Decodes Google App Script's ScriptApp.getOAuthToken()
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
        return User(id=userinfo["sub"], email=userinfo["email"])
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid OAuth Token",
        )


# Require authentication for every endpoint
app = FastAPI(dependencies=[Security(decode_oauth_token)])
