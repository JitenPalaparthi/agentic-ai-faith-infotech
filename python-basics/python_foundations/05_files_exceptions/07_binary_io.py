from io import BytesIO
buf = BytesIO()
buf.write(b"ABC")
buf.seek(0)
print(buf.read())
