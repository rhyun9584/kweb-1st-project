from flask import Flask
from flask.templating import render_template
from flask_migrate import Migrate, migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # DB 연결
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # blueprint (청사진) -> routing
    from .views import main_views, auth_views, user_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(user_views.bp)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404

    return app