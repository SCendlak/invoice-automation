# Generated by Django 5.0.6 on 2024-06-20 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generate_invoice', '0005_products_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='cena',
            field=models.FloatField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='waga',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
