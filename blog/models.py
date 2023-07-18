from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy
from .managers import CustomUserManager
STATUS = (
    (0, 'DRAFT'),
    (1, 'PUBLISHED')
)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(gettext_lazy("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    profile_image = models.ImageField(null=True, upload_to="media")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class TechStack(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, upload_to="media")
    technology = models.ManyToManyField(TechStack)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Images(models.Model):
    image = models.ImageField(upload_to="adventures")
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']


