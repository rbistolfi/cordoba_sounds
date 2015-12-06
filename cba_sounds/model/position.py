# coding: utf-8


from cba_sounds.model import db


class PositionMixin:

    meta = {
        "abstract": True
    }

    position = db.PointField()
