import os 
from pathlib import Path 
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent /".env", override=True)

DATABASE_URL = os.environ["DATABASE_URL"]

TOTAL_PERSONAS= int(os.getenv("TOTAL_PERSONAS", 100000))

BATCH_SIZE= int(os.getenv("BATCH_SIZE", 1000))

FAKER_LOCALE = os.getenv("FAKER_LOCALE", "es_CO")

if TOTAL_PERSONAS <= 0:
    raise ValueError("TOTAL_PERSONAS debe ser mayor que 0")

if BATCH_SIZE <= 0:
    raise ValueError("BATCH_SIZE debe ser mayor que 0")

