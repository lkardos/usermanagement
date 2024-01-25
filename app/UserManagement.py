class User:
    def __init__(self, username=None, email=None, password=None, user=None):
        if user is not None:
            self.username = user.username
            self.email = user.email
            self._password_hash = user._password_hash
        else:
            # TODO: Validate fields
            self.username = username
            self.email = email
            self._password_hash = hash_password(password)


class UserRepository:
    def __init__(self):
        self.users = []  # TODO: Use something more persistent

    def add(self, user):
        self.users.append(user)  # TODO: Check uniqueness of the username

    def get_user(self, username):
        return User(user=next(user for user in self.users if user.username == username))  # TODO: Throw better exception than StopIteration

    def list_users(self):
        return [User(user=user) for user in self.users]


def hash_password(password):
    return password  # TODO: Do some real hashing
