# coding: utf-8


from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "cbasounds"}
app.config["SECRET_KEY"] = "2po89gvuhpfvnhp98r5phnf"


db = MongoEngine(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def register_blueprints():
    import views #NOQA
    app.register_blueprint(views.reports)


if __name__ == "__main__":
    register_blueprints()
    app.run(debug=True, port=8081, host="0.0.0.0")
