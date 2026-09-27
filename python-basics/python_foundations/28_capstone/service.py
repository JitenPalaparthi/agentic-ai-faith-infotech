class CourseService:
    def __init__(self, repo):
        self.repo = repo

    def create(self, title, duration_hours):
        if duration_hours <= 0:
            raise ValueError("duration_hours must be positive")
        return self.repo.create(title, duration_hours)
