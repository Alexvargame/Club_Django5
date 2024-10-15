from django.db import models
from django.contrib.auth.models import User

from .enums import Status, Role





class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=5000)
    repo_link = models.CharField(max_length=255)
    status = models.CharField(choices=Status, default=Status.OPEN, max_length=15)
    author_role = models.CharField(choices=Role, default=Role.BACKEND, max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    categories = models.ManyToManyField("Category", related_name="projects")
    stacks = models.ManyToManyField("Stack", related_name="projects")

    def __str__(self):
        return self.name

    def get_categories(self):
        print(self.categories.all())
        return [cat for cat in self.categories.all()]

    def get_stacks(self):
        return [st for st in self.stacks.all()]