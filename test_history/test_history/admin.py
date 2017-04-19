# coding=utf-8
from django.contrib import admin

from test_history.models import *


class MyTestJobAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'last_edit', 'job_url')
    ordering = ('timestamp',)
    search_fields = ['status', 'timestamp']


class MyTestCaseResultAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'last_edit', 'test_case')
    ordering = ('timestamp', 'status')
    filtering = ('status',)
    search_fields = ['job_name', 'job_title']


class MyTestRunResultAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'last_edit', 'name')
    filter_horizontal = ('test_results',)  # Better view for M2M fields


admin.site.register(TestJob, MyTestJobAdmin)
admin.site.register(TestCase)
admin.site.register(TestCaseResult, MyTestCaseResultAdmin)
admin.site.register(TestRunResult, MyTestRunResultAdmin)
