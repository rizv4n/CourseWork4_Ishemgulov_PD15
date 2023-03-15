from data.dao.models.user import User


class UserDAO:
    """
    CRUD User
    """
    def __init__(self, session):
        self.session = session

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def create(self, data):
        user = User(**data)

        self.session.add(user)
        self.session.commit()

        return user

    def update(self, user):
        self.session.add(user)
        self.session.commit()

        return user

    def delete(self, email):
        user = self.get_by_email(email)

        self.session.delete(user)
        self.session.commit()
