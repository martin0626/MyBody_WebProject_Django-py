# Generated by Django 4.0.1 on 2022-04-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0004_navigation_fa_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='navigation',
            name='visible',
            field=models.CharField(choices=[('authenticate', 'authenticate'), ('anonymous', 'anonymous'), ('all', 'all')], default='all', max_length=12),
        ),
    ]
