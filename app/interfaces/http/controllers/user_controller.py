from flask import Blueprint, request

user = Blueprint("user", __name__)

@user.route("/signup")
def main():
	data = request.get_json() or {}
	username = data.get("username")
	password = data.get("password")

	return "This endpoint will be used to register users"