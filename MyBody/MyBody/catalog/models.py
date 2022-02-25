from django.core.validators import MinLengthValidator
from django.db import models

from MyBody.catalog.validators import MaxSizeImageValidator
from MyBody.users.models import MyBodyUser


class Article(models.Model):
    MAX_SIZE_FOR_IMAGE = 5
    TITLE_MAX_LENGTH = 20
    TITLE_MIN_LENGTH = 5
    DESCRIPTION_MIN_LENGTH = 10

    TYPE_CHOICE_NUTRITION = 'nutrition'
    TYPE_CHOICE_TRAINING = 'training'
    TYPE_CHOICE_FREE_TIME = 'free time'
    TYPE_CHOICE_OTHER = 'other'

    TYPE_CHOICES = (
        (TYPE_CHOICE_NUTRITION, 'Nutrition'),
        (TYPE_CHOICE_TRAINING, 'Training'),
        (TYPE_CHOICE_FREE_TIME, 'Free Time'),
        (TYPE_CHOICE_OTHER, 'Other'),
    )

    type = models.CharField(
        max_length=max([len(choice) for choice, x in TYPE_CHOICES]),
        choices=TYPE_CHOICES,
    )
    title = models.CharField(
        validators=[MinLengthValidator(TITLE_MIN_LENGTH)],
        max_length=TITLE_MAX_LENGTH
    )
    description = models.TextField(
        validators=[MinLengthValidator(DESCRIPTION_MIN_LENGTH)],
    )
    image = models.ImageField(
        upload_to='media/articles',
        validators=[MaxSizeImageValidator(MAX_SIZE_FOR_IMAGE)]
    )
    owner = models.ForeignKey(
        MyBodyUser,
        on_delete=models.CASCADE,
        default=None,
    )

    class Meta:
        ordering = ['title']


class LikeArticle(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        MyBodyUser, on_delete=models.CASCADE,
        null=True,
    )


class CommentModel(models.Model):
    owner = models.ForeignKey(
        MyBodyUser,
        on_delete=models.CASCADE,
        default=None,
    )
    content = models.TextField()

