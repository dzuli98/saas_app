from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db -> table
    # id -> hidden -> primary key -> autofield -> 1, 2, 3...
    path = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)