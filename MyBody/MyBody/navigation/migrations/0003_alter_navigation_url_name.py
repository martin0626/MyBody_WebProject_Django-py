# Generated by Django 4.0.1 on 2022-04-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0002_navigation_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigation',
            name='url_name',
            field=models.CharField(choices=[('home', 'home'), ('login', 'login'), ('register', 'register'), ('logout', 'logout'), ('catalog', 'catalog'), ('search catalog', 'search catalog'), ('profile details', 'profile details')], max_length=15),
        ),
    ]
