from app.infrastructure.database.db import db
from app.infrastructure.database.models.user import UserModel

class SqlAlchemyUserRepository(UserRepository):
    def add(self, user: User) -> User:
        model = UserModel.from_entity(user)
        db.session.add(model)
        db.session.commit()
        return model.to_entity()