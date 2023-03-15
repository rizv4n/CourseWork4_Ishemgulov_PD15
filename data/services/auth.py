from flask import abort
from data.services.user import UserService
from data.utils.auth_utils import get_hash, compare_password, generate_tokens, decode_refresh_token


class AuthService:
    """
    Бизнес логика для работы с авторизацией пользователей
    """
    def __init__(self, user_services: UserService):
        self.user_service = user_services

    def get_by_email(self, email):
        return self.user_service.get_by_email(email)

    def create(self, data):
        data["password"] = get_hash(data.get("password"))
        return self.user_service.create(data)

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.get_by_email(email)

        if user is None:
            raise abort(404)

        if not is_refresh:
            if not compare_password(user.password, password):
                abort(400)

        data = {
            "email": email,
            "password": password
        }

        return generate_tokens(data)

    def approve_refresh_token(self, token):
        email = decode_refresh_token(token)
        return self.generate_tokens(email, None, is_refresh=True)
