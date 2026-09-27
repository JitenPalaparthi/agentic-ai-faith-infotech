import hashlib, os

password = b"trainer-password"
salt = os.urandom(16)
digest = hashlib.pbkdf2_hmac("sha256", password, salt, 200_000)
print("salt:", salt.hex())
print("digest:", digest.hex())
