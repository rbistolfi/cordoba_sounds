# coding: utf-8


"""View services"""


from flask import render_template
from flask.views import View
from flask_security.decorators import login_required, roles_accepted


def staff_required(func):
    """A view decorator that accepts admin and staff users"""
    return roles_accepted("admin", "staff")(func)


def admin_required(func):
    """A view decorator that accepts admin users only"""
    return roles_accepted("admin")(func)


class TemplateView(View):

    def __init__(self, template_name):
        self.template_name = template_name

    def dispatch_request(self):
        return render_template(self.template_name)
