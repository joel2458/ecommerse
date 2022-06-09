# Generated by Django 4.0.4 on 2022-05-28 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommersApp', '0003_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(null=True, upload_to='product_image/'),
        ),
        migrations.CreateModel(
            name='product_multimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multimage', models.ImageField(blank=True, null=True, upload_to='multi/image')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommersApp.category')),
            ],
        ),
    ]
