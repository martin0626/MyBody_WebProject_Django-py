# Generated by Django 4.0.1 on 2022-02-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletypes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/articles_type'),
        ),
    ]
