import crum
from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Navigation(models.Model):
    TITLE_MAX_LEN = 20
    FA_MAX_LEN = 200
    PAGE_CHOICES = (
        ('home', 'home'),
        ('login', 'login'),
        ('register', 'register'),
        ('logout', 'logout'),
        ('catalog', 'catalog'),
        ('search catalog', 'search catalog'),
        ('profile details', 'profile details'),
        ('create article', 'create article'),
    )

    VISIBLE_CHOICES = (
        ('authenticate', 'authenticate'),
        ('anonymous', 'anonymous'),
        ('all', 'all'),

    )

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        null=True,
        blank=True,
    )

    left_side = models.BooleanField(
        default=True
    )

    url_name = models.CharField(
        max_length=max([len(choice) for _, choice in PAGE_CHOICES]),
        choices=PAGE_CHOICES,
    )

    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    is_active = models.BooleanField(
        default=True,
    )

    fa_icon = models.CharField(
        max_length=FA_MAX_LEN,
        blank=True,
        null=True,
    )
    visible = models.CharField(
        max_length=max([len(choice) for _, choice in VISIBLE_CHOICES]),
        choices=VISIBLE_CHOICES,
        default='all',
    )

    my_order = models.PositiveSmallIntegerField(
        default=0,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        if self.url_name == 'profile details':
            user = crum.get_current_user()
            return reverse(self.url_name, args=[str(user.id)])
        return reverse(self.url_name)

    class Meta:
        ordering = ['my_order']
