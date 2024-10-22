# Generated by Django 5.0.6 on 2024-07-02 16:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("generate_invoice", "0007_alter_products_cena_alter_products_waga"),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoice",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("index", models.CharField(blank=True, max_length=255, null=True)),
                ("date", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
