# coding: utf-8


import os

from flask import Flask, render_template
from flask_mail import Mail

from cba_sounds import settings
from cba_sounds.model import db
from cba_sounds.model.util import setup_user
from cba_sounds.views.util import register_blueprints


def create_app(config):
    """Create the application object"""
    app = Flask(__name__)
    app.config.from_object(config)
    mail = Mail(app)

    db.init_app(app)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    register_blueprints(app)
    setup_user(app, db)

    return app


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app = create_app(settings)
    app.run(debug=True, port=int(port), host="0.0.0.0")
