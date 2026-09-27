user_id = 10
safe_sql = "SELECT * FROM users WHERE id = %s"
params = (user_id,)
print(safe_sql, params)
print("Use parameterized queries; never concatenate untrusted input into SQL.")
