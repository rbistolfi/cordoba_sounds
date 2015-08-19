# coding: utf-8


from app import db


class PositionMixin:

    meta = {
        "abstract": True        
    }
    
    position = db.PointField()
