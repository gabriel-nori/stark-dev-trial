from dotenv import load_dotenv
import os

env_file_path = os.getcwd() + "/.env"

env_loaded = load_dotenv(dotenv_path=env_file_path, override=True)

LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

API_ROOT = os.getenv("API_ROOT", "localhost/")