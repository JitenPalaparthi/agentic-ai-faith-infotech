class UserRepository:
    def __init__(self):
        self.data = {}
    def save(self, user):
        self.data[user["id"]] = user
    def get(self, user_id):
        return self.data.get(user_id)

repo = UserRepository()
repo.save({"id": 1, "name": "Ada"})
print(repo.get(1))
