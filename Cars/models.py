from django.db import models
from django.urls import reverse


# Create your models here.
class Cars(models.Model):
    Brand = models.CharField(max_length=50)
    model_name = models.CharField(max_length=75)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to = "static/carImages")

    def __str__(self):
        return self.Brand

    def get_absolute_url(self):
        return reverse("Home:change_image",args=[self.id])