class Service:
    def __init__(self, repo):
        self.repo = repo
    def find(self, user_id):
        return self.repo.get(user_id)

class FakeRepo:
    def get(self, user_id):
        return {"id": user_id}

print(Service(FakeRepo()).find(10))
