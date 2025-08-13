from flask_sqlalchemy import SQLAlchemy
from app.infrastructure.database.config import DatabaseConfig

db = SQLAlchemy()

def init_db(app):
	
	config = DatabaseConfig()

	connection_string = f"{config.mysql_user}:{config.mysql_password}@{config.mysql_endpoint}/{config.mysql_database}"

	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}'.format(connection_string)

	db.init_app(app)