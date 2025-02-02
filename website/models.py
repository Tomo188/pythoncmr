from django.db import models

# Create your models here.
from django.db import models
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    adress=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=20)
    def __str__(self) -> str:
        return (f"{self.first_name} {self.last_name}")
