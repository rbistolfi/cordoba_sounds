# coding: utf-8


from flask.ext.security import MongoEngineUserDatastore, Security
from cba_sounds.model.user import User, Role


def setup_user(app, db):
    """Setup user system in app"""

    user_datastore = MongoEngineUserDatastore(db, User, Role)
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
