from dotenv import load_dotenv
import os
load_dotenv()
print("APP_ENV =", os.getenv("APP_ENV", "development"))
