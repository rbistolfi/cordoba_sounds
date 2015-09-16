# coding: utf-8

import json

from flask import Blueprint, request, render_template, url_for
from flask.views import MethodView, View

from response import JsonResponse
from report import Report


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
        reports = Report.objects.only("position").all()
        response = {
            reports: [r.as_dict() for r in reports]
        }
        return JsonResponse(response, status=200)


class DetailView(MethodView):

    def get(self, id):
        report = Report.objects.get_or_404(id=id)
        response = {"report": report.as_dict()}
        return JsonResponse(response, status=200)


reports = Blueprint("reports", __name__, template_folder="templates")
reports.add_url_rule("/", view_func=ListView.as_view("report_list"))
reports.add_url_rule("/anon", view_func=AnonListView.as_view("anon_report_list"))
reports.add_url_rule("/<id>/", view_func=DetailView.as_view("report_detail"))
reports.add_url_rule("/new", view_func=TemplateView.as_view("new_report", template_name="index.html"))
reports.add_url_rule("/admin", view_func=TemplateView.as_view("admin", template_name="admin.html"))
reports.add_url_rule("/detail", view_func=TemplateView.as_view("detail", template_name="detail.html"))
