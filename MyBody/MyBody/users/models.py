from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from MyBody.catalog.validators import MaxSizeImageValidator
from MyBody.users.managers import MyBodyUserManager
from MyBody.users.validators import validate_phone_number_min_length


class MyBodyUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MIN_LEN = 2
    EMAIL_MIN_LEN = 5

    email = models.EmailField(
        unique=True,
        validators=[MinLengthValidator(EMAIL_MIN_LEN)],
    )
    username = models.CharField(
        unique=True,
        max_length=15,
        validators=[MinLengthValidator(USERNAME_MIN_LEN)],
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    objects = MyBodyUserManager()

    def __str__(self):
        return self.username


class Profile(models.Model):
    PICTURE_MAX_SIZE = 5
    DESCRIPTION_MIN_LEN = 5

    MALE_GENDER_CHOICE = 'Male'
    FEMALE_GENDER_CHOICE = 'Female'

    GENDER_CHOICES = (
        (MALE_GENDER_CHOICE, 'Male'),
        (FEMALE_GENDER_CHOICE, 'Female'),
    )

    user = models.OneToOneField(
        MyBodyUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    picture = models.ImageField(
        upload_to='media/profile_pics',
        null=True,
        blank=True,
        validators=[MaxSizeImageValidator(PICTURE_MAX_SIZE)],
    )

    birth_date = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        max_length=100,
        null=True,
        blank=True,
        validators=[MinLengthValidator(DESCRIPTION_MIN_LEN)]
    )

    phone_for_contact = models.IntegerField(
        null=True,
        blank=True,
        validators=[validate_phone_number_min_length],
    )

    gender = models.CharField(
        max_length=max([len(gender) for _, gender in GENDER_CHOICES]),
        choices=GENDER_CHOICES,
        null=True,
        blank=True,
    )

    @property
    def age(self):
        today = datetime.today()
        years = today.year - self.birth_date.year
        if today.month < self.birth_date.month or (
                today.month == self.birth_date.month and today.day < self.birth_date.day):
            years -= 1
        return years

    def __str__(self):
        return self.user.username
