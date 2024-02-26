from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField()
    time_date = models.DateTimeField()
    skill = models.CharField(max_length=255)
    job_type = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.title

