import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from the .env file

# Access the environment variable
environment = os.getenv('ENVIRONMENT')
print(f"Current Environment: {environment}")

