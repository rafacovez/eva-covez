from django.db import models


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class Testimony(models.Model):
    author = models.CharField(max_length=30)
    profession = models.CharField(max_length=50)
    message = models.TextField(max_length=150)
    avatar = models.ImageField(upload_to="reviewers/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author


class Experience(models.Model):
    company = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    logo = models.ImageField(upload_to="companies/", blank=True, null=True)

    def __str__(self):
        return f"{self.role} at {self.company}"


class ContactOption(models.Model):
    PLATFORM_CHOICES = [
        ("email", "Email"),
        ("whatsapp", "WhatsApp"),
        ("other", "Other"),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    value = models.CharField(max_length=255)  # email/phone/URL
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.platform}: {self.value}"
