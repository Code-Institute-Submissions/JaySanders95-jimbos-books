# Generated by Django 3.2.3 on 2023-12-23 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20231219_1929'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='sku',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]