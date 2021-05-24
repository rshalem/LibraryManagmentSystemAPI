from categories.models import Categories
import categories
from django.db import models
import uuid

from authors.models import Authors
from categories.models import Categories

# Create your models here.
class Books(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    book_name = models.CharField(max_length=255, unique=True)
    published_date = models.DateField(auto_now_add=True)
    authors = models.ManyToManyField(Authors)
    categories = models.ManyToManyField(Categories)

    class Meta:
        verbose_name_plural = 'book'

    def __str__(self):
        return self.book_name

    @property
    def get_categories(self): # analytics api
        return self.categories_set.all()