import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

MONGODB_URI = os.getenv('MONGODB_URI')
if not MONGODB_URI:
    raise ValueError("MONGODB_URI environment variable is not set. Please check your .env file.")

OUTPUT_FOLDER = "output"
SUPPORTED_LANGUAGES = ["Python", "Android", "React", "Flutter"]