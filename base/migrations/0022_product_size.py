# Generated by Django 5.0.3 on 2024-03-07 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_remove_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='Small', max_length=50),
        ),
    ]
