# Generated by Django 4.2 on 2023-06-16 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_rename_products_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='abouts',
            name='services',
            field=models.TextField(default=None),
        ),
    ]
