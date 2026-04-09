import os

SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE_ME_IN_PRODUCTION_use_openssl_rand_hex_32")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

raw_db_url = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./buildpro.db")
if raw_db_url.startswith("postgres://"):
    DATABASE_URL = raw_db_url.replace("postgres://", "postgresql+psycopg://", 1)
elif raw_db_url.startswith("postgresql://"):
    DATABASE_URL = raw_db_url.replace("postgresql://", "postgresql+psycopg://", 1)
else:
    DATABASE_URL = raw_db_url

# AI keys — leave blank, user fills later
AI_PROVIDER = os.getenv("AI_PROVIDER", "")  # openai | gemini | custom
AI_API_KEY = os.getenv("AI_API_KEY", "")
AI_ENDPOINT = os.getenv("AI_ENDPOINT", "")

# UPI config — leave blank, user fills later
UPI_MERCHANT_ID = os.getenv("UPI_MERCHANT_ID", "")
UPI_MERCHANT_NAME = os.getenv("UPI_MERCHANT_NAME", "Samarth Developers")
UPI_VPA = os.getenv("UPI_VPA", "")  # e.g. merchant@upi

APP_NAME = "BuildPro API"
APP_VERSION = "3.0.0"
