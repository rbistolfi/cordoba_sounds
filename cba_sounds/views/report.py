# coding: utf-8

from flask import Blueprint, request, render_template, url_for
from flask.views import MethodView, View
from flask_security.decorators import login_required, roles_accepted

from cba_sounds.model.report import Report
from cba_sounds.views.response import JsonResponse
from cba_sounds.views.util import admin_required, staff_required, TemplateView


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


reports = Blueprint("reports", __name__, template_folder="templates")

# Public, anonymous reports
reports.add_url_rule("/api/report/anon", view_func=AnonListView.as_view("anon_report_list"))

# Staff required, report list and details
reports.add_url_rule("/api/report/<id>/", view_func=staff_required(DetailView.as_view("report_detail")))
reports.add_url_rule("/api/report", view_func=staff_required(ListView.as_view("report_list")))
reports.add_url_rule("/admin", view_func=staff_required(TemplateView.as_view("admin", template_name="admin.html")))
reports.add_url_rule("/detail", view_func=staff_required(TemplateView.as_view("detail", template_name="detail.html")))

# Public pages
reports.add_url_rule("/", view_func=TemplateView.as_view("index", template_name="index.html"))
reports.add_url_rule("/new", view_func=TemplateView.as_view("new_report", template_name="new.html"))
reports.add_url_rule("/report_created", view_func=TemplateView.as_view("report_created", template_name="report_created.html"))
