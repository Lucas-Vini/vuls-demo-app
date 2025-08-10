from flask import Flask
from app.interfaces.http.controllers.ping_controller import ping
from app.interfaces.http.controllers.user_controller import user


ACTIVE_ENDPOINTS = (
	("/", ping),
	("/", user)
	)

def create_app():
	app = Flask(__name__)
	
	# accepts both /endpoint and /endpoint/ as valid URLs
	app.url_map.strict_slashes = False

	for url, blueprint in ACTIVE_ENDPOINTS:
		app.register_blueprint(blueprint, url_prefix=url)

	return app