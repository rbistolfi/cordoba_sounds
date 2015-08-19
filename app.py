# coding: utf-8


import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": os.environ.get("MONGOLAB_URI", "cbasounds")}
app.config["SECRET_KEY"] = "2po89gvuhpfvnhp98r5phnf"


db = MongoEngine(app)


def register_blueprints():
    import views #NOQA
    app.register_blueprint(views.reports)


if __name__ == "__main__":
    register_blueprints()
    port = os.environ.get("PORT", 5000)
    app.run(debug=True, port=port, host="0.0.0.0")
