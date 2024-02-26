from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
    company_address = models.TextField()
    company_bio = models.TextField(blank=True, null=True)
    website = models.URLField()
    contact_number = models.CharField(max_length=10)
    email = models.EmailField()
    type = models.CharField(max_length=15, default='company')


    def __str__(self):
        return self.company_name

