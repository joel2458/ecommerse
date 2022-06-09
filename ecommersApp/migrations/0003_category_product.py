# Generated by Django 4.0.4 on 2022-05-26 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommersApp', '0002_remove_user_member_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product_image/')),
                ('price', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=40)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommersApp.category')),
            ],
        ),
    ]
