import os
from dotenv import load_dotenv

load_dotenv()

SMS_SETTINGS = {
    "API_ID": os.getenv("SMSRU_API_ID"),
    "FROM": os.getenv("SMSRU_FROM"),
}
