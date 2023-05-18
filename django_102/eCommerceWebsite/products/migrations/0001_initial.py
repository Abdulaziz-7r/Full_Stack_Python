# Generated by Django 4.2 on 2023-05-18 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Seller",
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
                ("name", models.CharField(help_text="seller name", max_length=50)),
                (
                    "phone",
                    models.CharField(help_text="seller contact number", max_length=20),
                ),
                (
                    "email",
                    models.EmailField(help_text="seller contact email", max_length=254),
                ),
                ("profile", models.TextField(blank=True, help_text="seller's profile")),
                ("photo", models.ImageField(upload_to="seller/photos/")),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(help_text="product's name", max_length=50)),
                (
                    "description",
                    models.TextField(blank=True, help_text="product's description"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, help_text="product's price", max_digits=5
                    ),
                ),
                ("photo", models.ImageField(upload_to="product/photos/")),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="products.seller",
                    ),
                ),
            ],
        ),
    ]