import uuid
from django.db import models

class User(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        )
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user"