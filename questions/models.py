from django.db import models
from django.contrib.auth.models import User

# Create your models here.

LEVEL_CHOICES = [
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard')
]
CATEGORY_CHOICES = [
    ('complexity', 'Space & Time Complexity'),
    ('array', 'Arrays'),
    ('linked_list', 'Linked Lists'),
    ('stacks', 'Stacks'),
    ('queues', 'Queues'),
    ('trees', 'Trees'),
    ('graphs', 'Graphs'),
    ('heaps', 'Heaps'),
    ('algos', 'Algorithms')
]

class Question(models.Model):
    question = models.TextField(max_length=1048)
    answer = models.CharField(max_length=512)
    level = models.CharField(max_length=8, choices=LEVEL_CHOICES)
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Discussion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)