# coding: utf-8


import os
from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine
from flask.ext.security import Security, MongoEngineUserDatastore
from flask_mail import Mail


app = Flask(__name__)


# Mongo settings
app.config["MONGODB_SETTINGS"] = {
    "HOST": os.environ.get("MONGOLAB_URI", None),
    "DB": "cbasounds"
}

# App secret
app.config["SECRET_KEY"] = "2po89gvuhpfvnhp98r5phnf"

# Mail settings
app.config['MAIL_SERVER'] = 'pop.faudi.unc.edu.ar'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'youremail@institution.edu'
app.config['MAIL_PASSWORD'] = 'changeme'
mail = Mail(app)

# Security settings
app.config['SECURITY_EMAIL_SENDER'] = 'youremail@institution.edu'
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = 'your salt'
app.config['SECURITY_CONFIRMABLE'] = True
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_RECOVERABLE'] = True
app.config['SECURITY_CHANGEABLE'] = True


db = MongoEngine(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def register_blueprints():
    import views #NOQA
    app.register_blueprint(views.reports)


def setup_user():
    import user #NOQA

    user_datastore = MongoEngineUserDatastore(db, user.User, user.Role)
    security = Security(app, user_datastore)

    @app.before_first_request
    def setup_user_and_roles():
        admin = user_datastore.find_user(email="rbistolfi@gmail.com")
        if not admin:
            admin = user_datastore.create_user(email="rbistolfi@gmail.com", password="changeme")

        a = user_datastore.find_or_create_role(name="admin", description="Site administrator")
        s = user_datastore.find_or_create_role(name="staff", description="Staff can manage reports")
        u = user_datastore.find_or_create_role(name="user", description="User can create reports and view owned reports")

        user_datastore.add_role_to_user(admin, "admin")

    return user_datastore, security


if __name__ == "__main__":
    port = os.environ.get("PORT", 5000)
    register_blueprints()
    user_datastore, security = setup_user()
    app.run(debug=True, port=int(port), host="0.0.0.0")
