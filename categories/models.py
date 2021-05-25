from django.db import models
import uuid

# Create your models here.
class Categories(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    category_name = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = 'category'
        
    def __str__(self):
        return self.category_name