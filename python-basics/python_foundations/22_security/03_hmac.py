import hmac, hashlib
key = b"secret"
msg = b"payload"
sig = hmac.new(key, msg, hashlib.sha256).hexdigest()
print(sig)
