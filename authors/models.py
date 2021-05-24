from re import VERBOSE
from django.db import models
import uuid

# Create your models here.
class Authors(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    author_name = models.CharField(max_length=255, unique=True)
    author_registered = models.DateTimeField(auto_now_add=True)
    bio = models.TextField()

    class Meta:
        ordering = ['author_name']
        verbose_name_plural = 'author'

    def __str__(self):
        return self.author_name