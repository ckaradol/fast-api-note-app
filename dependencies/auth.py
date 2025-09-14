from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from services.firebase import auth, map_firebase_error

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    token = credentials.credentials  
    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token["user_id"]
    except auth.InvalidIdTokenError:
        raise HTTPException(status_code=401, detail="Invalid ID token")
    except auth.ExpiredIdTokenError:
        raise HTTPException(status_code=401, detail="Token expired")
    except auth.RevokedIdTokenError:
        raise HTTPException(status_code=401, detail="Token revoked")
    except auth.UserDisabledError:
        raise HTTPException(status_code=403, detail="User account disabled")
    except Exception as e:
        code, msg = map_firebase_error(e)
        raise HTTPException(status_code=code, detail=msg)
