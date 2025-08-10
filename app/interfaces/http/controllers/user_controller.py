from flask import Blueprint

user = Blueprint("user", __name__)

@user.route("/signup")
def main():
	return "This endpoint will be used to register users"