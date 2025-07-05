import jwt
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from fastapi import HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
import httpx
from app.config.settings import get_settings

settings = get_settings()
security = HTTPBearer()

class Auth0Verifier:
    def __init__(self):
        self.domain = settings.auth0_domain
        self.audience = settings.auth0_audience
        self.algorithms = ["RS256"]
        self.jwks_url = f"https://{self.domain}/.well-known/jwks.json"
        self._jwks_cache = None
        self._cache_time = None

    async def get_jwks(self) -> Dict[str, Any]:
        """Get JSON Web Key Set from Auth0"""
        if self._jwks_cache is None or self._cache_expired():
            async with httpx.AsyncClient() as client:
                response = await client.get(self.jwks_url)
                response.raise_for_status()
                self._jwks_cache = response.json()
                self._cache_time = datetime.now()
        return self._jwks_cache

    def _cache_expired(self) -> bool:
        if self._cache_time is None:
            return True
        return datetime.now() - self._cache_time > timedelta(hours=1)

    async def verify_token(self, token: str) -> Dict[str, Any]:
        try:
            jwks = await self.get_jwks()

            unverified_header = jwt.get_unverified_header(token)
            kid = unverified_header.get("kid")

            if not kid:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token header"
                )

            key = None
            for jwk in jwks["keys"]:
                if jwk["kid"] == kid:
                    key = jwt.algorithms.RSAAlgorithm.from_jwk(jwk)
                    break

            if not key:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token key"
                )

            payload = jwt.decode(
                token,
                key,
                algorithms=self.algorithms,
                audience=self.audience,
                issuer=f"https://{self.domain}/"
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired"
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )

auth0_verifier = Auth0Verifier()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    payload = await auth0_verifier.verify_token(token)
    return payload