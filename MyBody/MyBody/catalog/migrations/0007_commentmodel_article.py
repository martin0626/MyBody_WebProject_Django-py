# Generated by Django 4.0.1 on 2022-03-02 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_article_options_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='article',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.article'),
        ),
    ]
