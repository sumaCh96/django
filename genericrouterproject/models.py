from django.db import models

class BaseModel(models.Model):
    created_date_time = models.DateTimeField(auto_now_add=True)
    update_date_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True