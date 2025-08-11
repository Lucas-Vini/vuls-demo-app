from werkzeug.security import generate_password_hash
from app.domain.repositories.user_repository import UserRepository
from app.domain.entities.user import User

def create_user(username: str, password: str, repo: UserRepository) -> User:
    password_hash = generate_password_hash(password)
    user = User(id=None, username=username, password_hash=password_hash)
    user = repo.add(user)
    return user