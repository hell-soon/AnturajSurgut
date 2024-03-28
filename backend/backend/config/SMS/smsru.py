import os
from dotenv import load_dotenv

load_dotenv()

SMS_SETTINGS = {
    "API_ID": os.getenv("SMS_RU_API_ID"),
    "FROM": os.getenv("SMSRU_FROM"),
}
