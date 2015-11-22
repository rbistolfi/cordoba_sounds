# coding: utf-8

from flask import Blueprint, request, render_template, url_for
from flask.views import MethodView, View
from flask_security.decorators import login_required, roles_accepted

from response import JsonResponse
from report import Report
from user import User, Role


class TemplateView(View):

    def __init__(self, template_name):
        self.template_name = template_name

    def dispatch_request(self):
        return render_template(self.template_name)


class ListView(MethodView):
    """List of reports"""

    def get(self):
        reports = Report.objects.all()
        response = {
            "reports": [r.as_dict() for r in reports]
        }
        return JsonResponse(response, status=200)

    def post(self):
        data_dict = request.get_json()
        report = Report(**data_dict)
        report.position = [float(s) for s in data_dict["position"]]
        report.save()
        url = url_for(".report_detail", id=str(report.id))
        response = {
            "report": report.as_dict(),
            "url": url
        }
        return JsonResponse(response, status=200)


class AnonListView(MethodView):
    """Similar to ListView but without personal data"""

    def get(self):
        fields = "address", "position", "severity", "noise_type"
        reports = Report.objects.only(*fields).all()
        response = {
            "reports": [r.as_dict() for r in reports]
        }
        return JsonResponse(response, status=200)


class DetailView(MethodView):
    """Get the full json document for a single report"""

    def get(self, id):
        report = Report.objects.get_or_404(id=id)
        response = {"report": report.as_dict()}
        return JsonResponse(response, status=200)


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


def staff_required(func):
    """A view decorator that accepts admin and staff users"""
    return roles_accepted("admin", "staff")(func)


def admin_required(func):
    """A view decorator that accepts admin users only"""
    return roles_accepted("admin")(func)


reports = Blueprint("reports", __name__, template_folder="templates")

# Public, anonymous reports
reports.add_url_rule("/api/report/anon", view_func=AnonListView.as_view("anon_report_list"))

# Staff required, report list and details
reports.add_url_rule("/api/report/<id>/", view_func=staff_required(DetailView.as_view("report_detail")))
reports.add_url_rule("/api/report", view_func=staff_required(ListView.as_view("report_list")))
reports.add_url_rule("/admin", view_func=staff_required(TemplateView.as_view("admin", template_name="admin.html")))
reports.add_url_rule("/detail", view_func=staff_required(TemplateView.as_view("detail", template_name="detail.html")))

# Admin required, user management
reports.add_url_rule("/api/user", view_func=admin_required(UserManagerView.as_view("user_list")))
reports.add_url_rule("/user", view_func=admin_required(TemplateView.as_view("user", template_name="user.html")))

# Public pages
reports.add_url_rule("/", view_func=TemplateView.as_view("index", template_name="index.html"))
reports.add_url_rule("/new", view_func=TemplateView.as_view("new_report", template_name="new.html"))
reports.add_url_rule("/report_created", view_func=TemplateView.as_view("report_created", template_name="report_created.html"))
