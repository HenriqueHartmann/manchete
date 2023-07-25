import uuid
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user", db_column="id_user")
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name} | {self.user.email}'


    class Meta:
        db_table = "profile"
