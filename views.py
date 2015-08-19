# coding: utf-8

import json

from flask import Blueprint, Response, request, redirect, url_for
from flask.views import MethodView

from response import JsonResponse
from report import Report


class ListView(MethodView):

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


class DetailView(MethodView):

    def get(self, id):
        report = Report.objects.get_or_404(id=id)
        response = {"report": report.as_dict()}
        return JsonResponse(response, status=200)


reports = Blueprint("reports", __name__, template_folder="templates")
reports.add_url_rule("/", view_func=ListView.as_view("report_list"))
reports.add_url_rule("/<id>/", view_func=DetailView.as_view("report_detail"))
