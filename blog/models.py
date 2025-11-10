from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(
        unique=True, max_length=220, blank=True
    )  # SEO friendly URLs
    author = models.ForeignKey("Profile", on_delete=models.CASCADE)
    content = models.TextField()
    excerpt = models.TextField(blank=True, null=True)  # for previews/snippets
    cover_image = models.ImageField(upload_to="posts/", blank=True, null=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    tags = models.ManyToManyField("Tag", blank=True)

    class Meta:
        ordering = ["-published_at"]

    def get_absolute_url(self):
        return reverse("post", args=[self.slug])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.status == "published" and not self.published_at:
            self.published_at = timezone.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profession = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to="authors/", blank=True, null=True)
    bio = models.TextField(blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def initials(self):
        return (self.first_name[0] + self.last_name[0]).upper()

    def __str__(self):
        return f"{self.user.username} Profile"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, max_length=60)

    def __str__(self):
        return self.name
