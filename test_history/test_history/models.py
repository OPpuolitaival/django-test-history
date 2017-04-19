# coding: utf-8
"""
Models
"""

from django.db import models


class TestJob(models.Model):
    """
    Test job
    """
    timestamp = models.DateTimeField('Added', auto_now_add=True, db_index=True)
    last_edit = models.DateTimeField('Last time edited', auto_now=True, null=True)
    job_name = models.CharField('Job name', max_length=255, blank=True, db_index=True, unique=True)
    job_url = models.CharField('Job url', max_length=255, blank=True, db_index=True)

    def __str__(self):
        return self.job_name

    class Meta(object):
        app_label = 'test_history'
        ordering = ['job_name']


class TestCase(models.Model):
    """
    Test case information
    """
    timestamp = models.DateTimeField('Added', auto_now_add=True, db_index=True)
    last_edit = models.DateTimeField('Last time edited', auto_now=True, null=True)
    name = models.CharField('Name', max_length=255, blank=True, db_index=True)
    classname = models.CharField('classname', max_length=255, blank=True, db_index=True)
    additional_info = models.TextField('Additional info', blank=True)

    def __str__(self):
        return self.name

    class Meta(object):
        app_label = 'test_history'
        ordering = ['timestamp']


class TestCaseResult(models.Model):
    """
    Test case result
    """
    timestamp = models.DateTimeField('Added', auto_now_add=True, db_index=True)
    last_edit = models.DateTimeField('Last time edited', auto_now=True, null=True)
    test_case = models.ForeignKey(TestCase, blank=True, verbose_name='Test case')

    PASSED = 0
    FAILED = 1
    SKIPPED = 1
    STATUS = (
        (PASSED, 'Passed'),
        (FAILED, 'Failed'),
        (SKIPPED, 'Skipped'),
    )
    status = models.PositiveIntegerField(choices=STATUS, default=PASSED, db_index=True)
    error_message = models.TextField('Error message', blank=True)
    additional_info = models.TextField('Additional info', blank=True)

    class Meta(object):
        app_label = 'test_history'
        ordering = ['timestamp']


class TestRunResult(models.Model):
    """
    One test execution in jenkins
    """
    timestamp = models.DateTimeField('Added', auto_now_add=True, db_index=True)
    last_edit = models.DateTimeField('Last time edited', auto_now=True, null=True)
    name = models.CharField('Name', max_length=255, blank=True, db_index=True)
    test_job = models.ForeignKey(TestJob, blank=True, verbose_name='Test job')
    test_results = models.ManyToManyField(TestCaseResult, blank=True, verbose_name='Test case results')


    PASSED = 0
    FAILED = 1
    STATUS = (
        (PASSED, 'Passed'),
        (FAILED, 'Failed'),
    )
    status = models.PositiveIntegerField(choices=STATUS, default=PASSED, db_index=True)
    additional_info = models.TextField('Additional info', blank=True)

    def __str__(self):
        return self.name

    class Meta(object):
        app_label = 'test_history'
        ordering = ['timestamp']
