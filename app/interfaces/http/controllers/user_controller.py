from flask import Blueprint, request
from app.infrastructure.database.repositories.user_repository_implementation import SqlAlchemyUserRepository

user = Blueprint("user", __name__)

@user.route("/signup")
def main():
	data = request.get_json() or {}
	username = data.get("username")
	password = data.get("password")

	sql_alchemy_user_repository = SqlAlchemyUserRepository()

	return "This endpoint will be used to register users"