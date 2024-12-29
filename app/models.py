from django.db import models

# Create your models here.

class GymUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)  # Store hashed passwords in production!
    plan = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class ContactInfo(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"Contact Info: {self.email}"


class Message(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name} - {self.email}"
