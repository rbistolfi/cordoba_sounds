# coding: utf-8


"""User model"""


from flask.ext.security import (
    RoleMixin,
    UserMixin,
)

from cba_sounds.model import db
from cba_sounds.model.serializable import SerializableMixin


class Role(db.Document, RoleMixin, SerializableMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)


class User(db.Document, UserMixin, SerializableMixin):
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

    def as_dict(self):
        d = super().as_dict()
        d["is_admin"] = self.has_role("admin")
        d["is_staff"] = self.has_role("staff")
        return d



