employees = [
    {"name": "A", "skills": ["Python", "SQL"]},
    {"name": "B", "skills": ["Go", "Python"]},
]
print([e["name"] for e in employees if "Python" in e["skills"]])
