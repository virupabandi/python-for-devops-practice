# Sensitive information like password, certificates, token, secrets, access key can be stored in env vars.

import os

print(os.getenv("password"))
print(os.getenv("apitoken"))

