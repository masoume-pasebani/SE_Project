# Generated by Django 4.2.8 on 2023-12-25 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='country',
        ),
    ]
