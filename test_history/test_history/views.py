# coding: utf-8
"""
Idea is to run this test and report results in test history
"""

from django.http import HttpResponse
from django.views.generic import TemplateView
from test_history.models import *
from django.http.response import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json


class MainPage(TemplateView):
    template_name = 'main_page.html'

    def get_context_data(self, **kwargs):
        context = super(MainPage, self).get_context_data(**kwargs)
        context.update({'jobs': TestJob.objects.all()})
        return context


@csrf_exempt
def post_result(request):
    required_keys = ['job_name', 'job_url', 'test_results']
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))

        # Validate
        for key in required_keys:
            if key not in data.keys():
                return HttpResponseBadRequest("{} key missing from content".format(key))

        test_job = TestJob.objects.filter(job_name=data['job_name']).first()

        # Create test job if not created yet
        if not test_job:
            test_job = TestJob.objects.create(
                job_name=data['job_name'],
                job_url=data['job_url']
            )

        if 'duration' in data.keys():
            # Save duration
            pass

        test_run_result = TestRunResult.objects.create(
            test_job=test_job,
        )

        for result in data['test_results']:

            tc = TestCase.objects.filter(name=result['case_name']).first()
            # Create if not created yet
            if not tc:
                tc = TestCase.objects.create(
                    name=result['case_name']
                )

            TestCaseResult.objects.create(
                test_case=tc,
                # TODO: Fix
                # status=TestCaseResult.PASSED
            )

        return HttpResponse()

    if request.method == "GET":
        return HttpResponse("Use post method for data sending")
    return HttpResponse()
