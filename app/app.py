import os

from fastapi import FastAPI, HTTPException, Security, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security.api_key import APIKeyHeader


async def authenticate(api_key: str = Security(APIKeyHeader(name="Authorization"))):
    """Validate the API_KEY as delivered by the Authorization header
    It is recommended to always set a unique XLWINGS_API_KEY as environment variable.
    Without an env var, it expects "DEVELOPMENT" as the API_KEY, which is insecure.
    """
    if api_key != os.getenv("XLWINGS_API_KEY", "DEVELOPMENT"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )


# Require the API_KEY for every endpoint
app = FastAPI(dependencies=[Security(authenticate)])

# Excel on the web and our Python backend are on different origins, so enable CORS.
# Google Sheets doesn't use CORS and will ingore this.
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https://.*.officescripts.microsoftusercontent.com",
    allow_methods=["POST"],
    allow_headers=["*"],
)
