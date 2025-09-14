import firebase_admin
import os
import json
from dotenv import load_dotenv
import base64
from firebase_admin import credentials, firestore, auth, exceptions as fb_exceptions
from google.api_core import exceptions as gcloud_exceptions
load_dotenv()
firebase_b64 = os.getenv("FIREBASE_CREDENTIALS_B64")

firebase_json = base64.b64decode(firebase_b64).decode()

cred_dict = json.loads(firebase_json)

cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred)
db = firestore.client()

def map_firebase_error(e: Exception) -> tuple[int, dict]:
    print(e)

    if isinstance(e, gcloud_exceptions.PermissionDenied):
        return 403, {"msg": "Firestore permission denied"}
    if isinstance(e, gcloud_exceptions.NotFound):
        return 404, {"msg": "Firestore document not found"}
    if isinstance(e, gcloud_exceptions.InvalidArgument):
        return 400, {"msg": "Invalid argument for Firestore request"}
    if isinstance(e, gcloud_exceptions.AlreadyExists):
        return 409, {"msg": "Document already exists"}
    if isinstance(e, gcloud_exceptions.DeadlineExceeded):
        return 504, {"msg": "Firestore request timed out"}
    if isinstance(e, gcloud_exceptions.Unauthenticated):
        return 401, {"msg": "Firestore unauthenticated request"}
    if isinstance(e, gcloud_exceptions.ResourceExhausted):
        return 429, {"msg": "Quota exceeded (too many requests)"}
    if isinstance(e, gcloud_exceptions.ServiceUnavailable):
        return 503, {"msg": "Firestore service unavailable"}
    if isinstance(e, gcloud_exceptions.Aborted):
        return 409, {"msg": "Operation aborted due to concurrency conflict"}
    if isinstance(e, gcloud_exceptions.InternalServerError):
        return 500, {"msg": "Internal Firestore server error"}
    if isinstance(e, gcloud_exceptions.FailedPrecondition):
        return 400, {"msg": "Firestore query requires an index or precondition failed"}
    if isinstance(e, gcloud_exceptions.Cancelled):
        return 499, {"msg": "Firestore request cancelled"}
    if isinstance(e, gcloud_exceptions.DataLoss):
        return 500, {"msg": "Unrecoverable Firestore data loss or corruption"}
    if isinstance(e, gcloud_exceptions.OutOfRange):
        return 400, {"msg": "Invalid Firestore range query"}

    if isinstance(e, fb_exceptions.FirebaseError):
        if e.code == "UNAVAILABLE":
            return 503, {"msg": "Firebase service unavailable"}
        if e.code == "INTERNAL":
            return 500, {"msg": "Internal Firebase error"}
        if e.code == "INVALID_ARGUMENT":
            return 400, {"msg": "Invalid argument in Firebase request"}
        if e.code == "PERMISSION_DENIED":
            return 403, {"msg": "Permission denied in Firebase"}
        if e.code == "NOT_FOUND":
            return 404, {"msg": "Requested Firebase resource not found"}
        if e.code == "ALREADY_EXISTS":
            return 409, {"msg": "Firebase resource already exists"}
        if e.code == "FAILED_PRECONDITION":
            return 400, {"msg": "Firebase request failed precondition"}
        if e.code == "RESOURCE_EXHAUSTED":
            return 429, {"msg": "Firebase quota exceeded"}
        if e.code == "ABORTED":
            return 409, {"msg": "Firebase operation aborted"}
        if e.code == "OUT_OF_RANGE":
            return 400, {"msg": "Firebase request out of range"}
        if e.code == "UNAUTHENTICATED":
            return 401, {"msg": "Unauthenticated Firebase request"}
        if e.code == "CANCELLED":
            return 499, {"msg": "Firebase request cancelled"}
        if e.code == "DATA_LOSS":
            return 500, {"msg": "Firebase data loss occurred"}
        return 500, {"msg": f"Firebase error: {e.code}"}

    return 500, {"msg": "Unexpected server error"}
