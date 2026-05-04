import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the SECRET_KEY from environment variables, or raise an error if not found
SECRET_KEY = os.getenv("SECRET_KEY")
if SECRET_KEY is None:
    raise ValueError("No SECRET_KEY set for the application")

# Database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
