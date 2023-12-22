from django.db import models

# Create your models here.
class Popular_Destinations(models.Model):
    img=models.ImageField(upload_to = 'pics')
    name=models.CharField(max_length = 250)
    description=models.TextField()
    price=models.CharField(max_length = 100)


    def __str__(self):
        return self.name

