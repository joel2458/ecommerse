# Generated by Django 4.0.4 on 2022-05-25 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommersApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_member',
            name='email',
        ),
    ]
