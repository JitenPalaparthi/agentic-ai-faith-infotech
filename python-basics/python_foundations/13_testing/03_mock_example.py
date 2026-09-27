from unittest.mock import Mock
repo = Mock()
repo.get_user.return_value = {"id": 1, "name": "Ada"}
print(repo.get_user(1))
repo.get_user.assert_called_once_with(1)
