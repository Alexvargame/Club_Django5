from django.db import models
from .enums import Grade

class Vacancy(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='project_vacancies')
    stack = models.ForeignKey('Stack', on_delete=models.CASCADE, related_name='tack_vacancies')
    grade = models.CharField(choices=Grade, default=Grade.JUNIOR, max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    closed_at = models.DateTimeField(null=True, blank=True)
