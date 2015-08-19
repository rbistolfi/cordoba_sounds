# coding: utf-8


import datetime

from app import db
from position import PositionMixin
from serializable import SerializableMixin


class Report(db.Document, PositionMixin, SerializableMixin):
    """A user submitted report"""

    created_at = db.DateTimeField(default=datetime.datetime.now)
    name = db.StringField(max_length=255)
    email = db.EmailField()
    telephone = db.StringField(max_length=255)
    address = db.StringField(max_length=255)
    city = db.StringField(max_length=255)
    province = db.StringField(max_length=255)
    noise_type = db.StringField(max_length=255)
    severity = db.IntField(default=0, choices=[1,2,3,4,5])
    comment = db.StringField(max_length=500)
    sound = db.StringField();

