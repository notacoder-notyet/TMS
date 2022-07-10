from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = (
    ('TODO', 'Todo'),
    ('IN_PROGRESS', 'In progress'),
    ('COMPLETED', 'Completed'),
)


class GlobalTask(models.Model):
    name = models.CharField(max_length=50)
    goal = models.CharField(max_length=100)
    objectives = models.ManyToManyField('Objectives', related_name='tasks')
    deadline = models.DateTimeField()
    costomer = models.CharField(max_length=50)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name


class Objectives(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True, null=True)
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='objectives')
    deadline = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
