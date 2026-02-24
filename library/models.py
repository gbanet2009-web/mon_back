from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    TYPE_CHOICES = [
        ('course', 'Cours'),
        ('exercise', 'Exercice'),
        ('bac', 'Sujet de bac'),
        ('bepc', 'Sujet de BEPC'),
    ]
    
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)
    class_level = models.CharField(max_length=20) # 6e, 5e, etc.
    pdf_url = models.URLField()
    price = models.IntegerField(default=0)
    doc_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='course')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.class_level})"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    credits = models.IntegerField(default=50)
    full_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'document')
