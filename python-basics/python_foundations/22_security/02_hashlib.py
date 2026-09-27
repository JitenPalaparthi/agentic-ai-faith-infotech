import hashlib
data = b"hello"
print(hashlib.sha256(data).hexdigest())
