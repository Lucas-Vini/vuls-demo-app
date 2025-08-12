from flask import Blueprint, request
from app.infrastructure.database.repositories.user_repository_implementation import SqlAlchemyUserRepository
from app.application.use_cases.create_user import create_user

user = Blueprint("user", __name__)

@user.route("/signup", methods=['GET', 'POST'])
def signup():
	data = request.get_json() or {}
	username = data.get("username")
	password = data.get("password")

	user_repository = SqlAlchemyUserRepository()
	user = create_user(username=username, password=password, repo=user_repository)

	return "This endpoint will be used to register users"