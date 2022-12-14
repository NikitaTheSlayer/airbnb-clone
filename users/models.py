import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.conf import settings
from django.utils.html import strip_tags
from django.urls import reverse
from django.shortcuts import redirect
from core import managers as core_managers
from django.template.loader import render_to_string

# Create your models here.


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
        (GENDER_OTHER, _("Other")),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_UKRAINIAN = "ua"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (
            LANGUAGE_UKRAINIAN,
            "Ukrainian",
        ),  # 1st value is going to database, the second value is for the admin (forms structures)
    )

    CURRENCY_USD = "usd"
    CURRENCY_UAH = "uah"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_UAH, "UAH"),
    )

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"
    LOGIN_KAKAO = "kakao"

    LOGIN_METHOD_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github"),
        (LOGIN_KAKAO, "Kakao"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_UKRAINIAN
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_UAH
    )
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_METHOD_CHOICES, default=LOGIN_EMAIL
    )
    objects = core_managers.CustomUserManager()

    def verify_email(self):
        if self.email_verified is False:
            unique_secret = uuid.uuid4().hex[:20]
            self.email_secret = unique_secret
            html_message = render_to_string(
                "emails/verify_email.html",
                {
                    "unique_secret": unique_secret,
                },
            )
            send_mail(
                "Verify Airbnb Account",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=False,
                html_message=html_message,
            )
            self.save()
        return

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})
