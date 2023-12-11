from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100, default='United States')
    phone = PhoneNumberField(null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name