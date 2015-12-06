# coding: utf-8


import json
from cba_sounds.model.position import PositionMixin


class SerializableMixin:

    blacklist = set(["created_at", "password"])

    def as_dict(self):

        d = {k: serialize(getattr(self, k)) for k in self._fields.keys() if k not in self.blacklist}

        if isinstance(self, PositionMixin):
            # flat position if needed
            try:
                position = self.position["coordinates"]
                d["position"] = position
            except TypeError:
                pass
        return d

    def as_json(self):
        return json.dumps(self.as_dict())


def serialize(v):
    """Serialize value"""
    if hasattr(v, "as_dict"):
        v = v.as_dict()
    elif isinstance(v, list):
        v = [serialize(i) for i in v]
    elif v is None or isinstance(v, bool):
        pass
    else:
        v = str(v)
    return v


