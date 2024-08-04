import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Try to get the MongoDB URI from environment variable
MONGODB_URI = os.getenv('MONGODB')

# If not found, try to read directly from .env file
if not MONGODB_URI:
    print("MONGODB_URI not found in environment variables. Attempting to read from .env file...")
    try:
        with open('.env', 'r') as env_file:
            for line in env_file:
                if line.startswith('MONGODB='):
                    MONGODB_URI = line.split('=', 1)[1].strip()
                    break
    except FileNotFoundError:
        print(".env file not found")
    except Exception as e:
        print(f"Error reading .env file: {e}")

if not MONGODB_URI:
    print("MONGODB_URI is still not set. Please check your .env file or environment variables.")
    # Instead of raising an error, you might want to set a default value or handle this gracefully
    MONGODB_URI = "mongodb://localhost:27017"  # Example fallback value

print(f"MONGODB_URI: {MONGODB_URI[:10]}...") # Print first 10 characters for debugging

OUTPUT_FOLDER = "output"
SUPPORTED_LANGUAGES = ["Python", "Android", "React", "Flutter"]