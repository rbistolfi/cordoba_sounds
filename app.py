# coding: utf-8


import os
from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "HOST": os.environ.get("MONGOLAB_URI", None),
    "DB": "cbasounds"
}
app.config["SECRET_KEY"] = "2po89gvuhpfvnhp98r5phnf"


db = MongoEngine(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def register_blueprints():
    import views #NOQA
    app.register_blueprint(views.reports)


register_blueprints()


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    app.run(debug=True, port=int(port), host="0.0.0.0")
