import os
import json
from google.oauth2 import service_account

def get_google_credentials():
    raw = os.getenv("GOOGLE_CREDENTIALS_JSON")
    if not raw:
        raise RuntimeError("Variável de ambiente GOOGLE_CREDENTIALS_JSON não encontrada.")
    
    raw = raw.replace("\\n", "\n")

    data = json.loads(raw)
    credentials = service_account.Credentials.from_service_account_info(data)

    return credentials
