import os
port = int(os.getenv("PORT", "8080"))
debug = os.getenv("DEBUG", "false").lower() == "true"
print(port, debug)
