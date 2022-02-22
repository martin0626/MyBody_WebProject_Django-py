from django.core.validators import MinLengthValidator
from django.db import models


class ArticleTypes(models.Model):
    TITLE_MAX_LEN = 20
    DESCRIPTION_MIN_LEN = 20

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    description = models.TextField(
        validators=[MinLengthValidator(DESCRIPTION_MIN_LEN)],
    )

    image = models.ImageField(
        upload_to='media/articles_type',
        null=True,
        blank=True,
    )
