from models.note import Note
error_responses = {
   
    400: {
        "description": "Bad Request - Invalid Firestore argument",
        "content": {
            "application/json": {
                "example": {
                    "status":400,
                    "success":False,
                    "detail": {"msg": "Invalid argument for Firestore request"}}
            }
        },
    },
    401: {
        "description": "Unauthorized - Invalid, expired or revoked token",
        "content": {
            "application/json": {
                "example": {
                        "status":401,
                    "success":False,
                    "detail": {"msg": "Invalid ID token"}}
            }
        },
    },
    403: {
        "description": "Forbidden - No permission or account disabled",
        "content": {
            "application/json": {
                "example": {
                       "status":403,
                    "success":False,
                    "detail": {"msg": "You are not allowed to update this note"}}
            }
        },
    },
    404: {
        "description": "Not Found - Document does not exist",
        "content": {
            "application/json": {
                "example": {
                       "status":404,
                    "success":False,
                    "detail": {"msg": "Note not found"}}
            }
        },
    },
    409: {
        "description": "Conflict - Document already exists",
        "content": {
            "application/json": {
                "example": {
                    "status":409,
                    "success":False,
                    "detail": {"msg": "Document already exists"}}
            }
        },
    },
    500: {
        "description": "Unexpected server error",
        "content": {
            "application/json": {
                "example": {
                        "status":500,
                    "success":False,
                    "detail": {"msg": "Unexpected server error"}}
            }
        },
    },
    503: {
        "description": "Firebase service unavailable",
        "content": {
            "application/json": {
                "example": {
                      "status":503,
                    "success":False,
                    "detail": {"msg": "Firebase service unavailable"}}
            }
        },
    },
    504: {
        "description": "Firestore request timed out",
        "content": {
            "application/json": {
                "example": {
                    "status":504,
                    "success":False,
                    "detail": {"msg": "Firestore request timed out"}}
            }
        },
    },
}
