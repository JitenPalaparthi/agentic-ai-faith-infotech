import subprocess
result = subprocess.run(["python3", "--version"], capture_output=True, text=True)
print(result.stdout or result.stderr)
