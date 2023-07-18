# Generated by Django 4.2 on 2023-06-14 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cdesc', models.TextField(default=None)),
                ('sdesc', models.TextField(default=None)),
                ('tname', models.TextField(default=None)),
                ('tphoto', models.TextField(default=None)),
                ('services', models.TextField(default=None)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.BigIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='product',
            name='warranty',
            field=models.TextField(default=None),
        ),
    ]
