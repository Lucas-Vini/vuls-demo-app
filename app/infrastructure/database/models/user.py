from app.infrastructure.database import db
from app.domain.entities.user import User

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def to_entity(self) -> User:
        return User(id=self.id, username=self.username, password_hash=self.password_hash)

    @classmethod
    def from_entity(cls, user: User) -> UserModel:
        kwargs = {"username": user.username, "password_hash": user.password_hash}
        if user.id is not None:
            kwargs["id"] = user.id
        return cls(**kwargs)
