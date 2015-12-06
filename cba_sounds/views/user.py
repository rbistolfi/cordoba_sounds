# coding: utf-8


"""User related views"""


from flask import Blueprint, request, render_template, url_for
from flask.views import MethodView
from flask_security.decorators import login_required, roles_accepted

from cba_sounds.model.user import User, Role
from cba_sounds.views.response import JsonResponse
from cba_sounds.views.util import admin_required, staff_required, TemplateView


class UserManagerView(MethodView):
    """User and Role information for user management"""

    def get(self):
        roles = Role.objects.all()
        users = User.objects.only("email", "roles", "active").all()
        response = {
            "roles": [r.as_dict() for r in roles],
            "users": [u.as_dict() for u in users],
        }
        return JsonResponse(response, status=200)

    def post(self):
        data_dict = request.get_json()
        user_id = data_dict.get("user_id")
        is_staff = data_dict.get("is_staff")
        user = User.objects.get_or_404(id=user_id)
        role = Role.objects.get_or_404(name="staff")

        if is_staff is True:
            user.roles.append(role)
            user.save()
        elif is_staff is False:
            user.roles.remove(role)
            user.save()

        response = {
            "user": user.as_dict(),
        }
        return JsonResponse(response, status=200)


users = Blueprint("users", __name__, template_folder="templates")
# Admin required, user management
users.add_url_rule("/api/user", view_func=admin_required(UserManagerView.as_view("user_list")))
users.add_url_rule("/user", view_func=admin_required(TemplateView.as_view("user", template_name="user.html")))

