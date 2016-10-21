# coding: utf-8


import json
from flask import Response


class JsonResponse(Response):

    def __init__(self, serializable_response, **kwargs):
        kwargs.pop("mimetype", None)
        response_string = json.dumps(serializable_response)
        super().__init__(response_string, mimetype="application/json", **kwargs)
