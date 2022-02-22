# Generated by Django 4.0.1 on 2022-02-18 11:24

import MyBody.catalog.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybodyuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, validators=[django.core.validators.MinValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='mybodyuser',
            name='username',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.MinValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True, validators=[django.core.validators.MinValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_pics', validators=[MyBody.catalog.validators.MaxSizeImageValidator(5)]),
        ),
    ]
