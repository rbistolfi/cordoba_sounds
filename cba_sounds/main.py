# coding: utf-8


"""Use the create_app() factory for creating the global app object. This is the
main entry point for deployed app.
"""


from cba_sounds import settings
from cba_sounds.app import create_app


app = create_app(settings)
