import random
import string


class User:
    def __init__(self, username=None, email=None, password=None, user=None):
        if user is not None:
            self._copy_from(user)
        else:
            # TODO: Validate fields
            self.username = username
            self.email = email
            self._password_hash = hash_password(password)
            self._token = None

    def _copy_from(self, user):
        self.username = user.username
        self.email = user.email
        self._password_hash = user._password_hash
        self._token = user._token

    def login(self, password):
        if self._password_hash != hash_password(password):
            raise Unauthorized

        self._token = generate_token()
        return self._token

    def logout(self, token):
        if self._token == token:
            self._token = None


class UserRepository:
    def __init__(self):
        self.users = []  # TODO: Use something more persistent

    def add(self, user):
        self.users.append(user)  # TODO: Check uniqueness of the username

    def update_user(self, user):
        key = next(key for key, current_user in enumerate(self.users) if current_user.username == user.username)
        self.users[key] = User(user=user)

    def get_user(self, username):
        return User(user=next(user for user in self.users if user.username == username))  # TODO: Throw better exception than StopIteration

    def get_user_by_token(self, token):
        user = next((user for user in self.users if user._token == token), None)
        if user is None:
            raise UserNotFound("Invalid token")
        return User(user=user)

    def list_users(self):
        return [User(user=user) for user in self.users]


def hash_password(password):
    return password  # TODO: Do some real hashing


def generate_token():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=256))


class Unauthorized(Exception):
    pass


class UserNotFound(Exception):
    pass
