from django.db import models
import uuid

# Create your models here.

class nudge_model(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='nudge_images/', null=True, blank=True)
    tagline = models.CharField(max_length=100)
    schedule = models.DateTimeField()
    description = models.TextField()
    moderator = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    rigor_rank = models.IntegerField()
