from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class_id = models.CharField(max_length=50, blank=True, null=True)
    credits = models.IntegerField(default=0)
    full_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username

class Course(models.Model):
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    pdf_url = models.URLField()
    class_id = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Exercise(models.Model):
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    pdf_url = models.URLField()
    class_id = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class BacSubject(models.Model):
    subject = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    pdf_url = models.URLField()

    def __str__(self):
        return self.title
