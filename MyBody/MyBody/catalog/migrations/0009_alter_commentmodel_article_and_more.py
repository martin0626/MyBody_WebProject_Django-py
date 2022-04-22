# Generated by Django 4.0.1 on 2022-04-20 12:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_commentmodel_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='article',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.article'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]