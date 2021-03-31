from django.db import models
from django.urls import reverse
# Create your models here.
class Company(models.Model):
    Name =models.CharField(max_length = 250)
    ceo = models.CharField(max_length = 60)
    location = models.CharField(max_length = 100)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
