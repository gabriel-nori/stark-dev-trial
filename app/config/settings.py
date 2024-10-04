from dotenv import load_dotenv
import base64
import os

env_file_path = os.getcwd() + "/.env"

env_loaded = load_dotenv(dotenv_path=env_file_path, override=True)

LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

API_ROOT = os.getenv("API_ROOT", "localhost/")

PRIVATE_KEY = base64.b64decode(os.getenv("PRIVATE_KEY", "").encode("ascii")).decode("ascii")

PROJECT_ID = os.getenv("PROJECT_ID")