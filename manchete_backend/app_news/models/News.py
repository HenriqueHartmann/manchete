import uuid

from django.db import models

from app_auth.models import Profile


class News(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="creator_user")
    published_by = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="publisher_user", null=True, blank=True)
    published = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    body = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}'


    class Meta:
        db_table = "news"
