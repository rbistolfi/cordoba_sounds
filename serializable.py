# coding: utf-8


import json
from position import PositionMixin


class SerializableMixin:

    blacklist = set(["created_at"])

    def as_dict(self):
        d = { k: str(getattr(self, k)) for k in self._fields.keys() if k not in self.blacklist }
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
