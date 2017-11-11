# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.contrib.auth.models import User
from django.db import models
from .validators import validate_file_extension

class course(models.Model):
    course_no = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=100, null=True, unique=True)
    credits = models.IntegerField(null=True)
    elective = models.NullBooleanField()
    semester = models.IntegerField(null=True)
    BRANCH = (
        ('CS', 'Computer Science'),
        ('IT', 'Information Technology'),
    )
    offered_to = models.CharField(max_length=20, null=True, choices=BRANCH)
    faculty = models.ManyToManyField(User)

    def __str__(self):
        return self.course_no

class CourseMaterial(models.Model):
    course_no = models.ForeignKey(course, to_field='course_no', null=True)
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='course/', validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    faculty = models.ForeignKey(User, null=True)

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    # def __str__(self):
    #     return os.path.basename(self.file.name)

class AssignmentMaterial(models.Model):
    course_no = models.ForeignKey(course, to_field='course_no', null=True)
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='assignment/')
    submission_last_date = models.DateTimeField(null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    faculty = models.ForeignKey(User, null=True)

    @property
    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return os.path.basename(self.file.name)
