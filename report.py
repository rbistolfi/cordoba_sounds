# coding: utf-8


import datetime

from app import db
from position import PositionMixin
from serializable import SerializableMixin


NOISE_TYPE_TO_STR = {
    "industry": "Industria",
    "activities": "Ocio y actividades recreativas",
    "commerce": "Actividades comerciales",
    "people": "Vecinos",
    "traffic": "Tráfico y medios de transporte",
    "work": "Obras",
    "other": "No lo sé / Otro"
}


class Report(db.Document, PositionMixin, SerializableMixin):
    """A user submitted report"""

    created_at = db.DateTimeField(default=datetime.datetime.now)
    name = db.StringField(max_length=255)
    email = db.EmailField()
    telephone = db.StringField(max_length=255)
    address = db.StringField(max_length=255)
    between_streets = db.StringField(max_length=255)
    city = db.StringField(max_length=255)
    province = db.StringField(max_length=255)
    noise_type = db.StringField(max_length=255)
    severity = db.IntField(default=0, choices=[1,2,3,4,5])
    comment = db.StringField(max_length=500)
    sound = db.StringField();

    def as_dict(self):
        """Report instance as dictionary.

        Overloads SerializableMixin.as_dict() for including noise_type_s, which
        is the noise_type as a human readable string.
        """
        d = super().as_dict()
        d["noise_type_s"] = NOISE_TYPE_TO_STR.get(self.noise_type)
        return d
