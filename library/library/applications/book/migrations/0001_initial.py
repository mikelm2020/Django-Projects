# Generated by Django 4.1.1 on 2022-09-17 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("author", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=30, verbose_name="Categoría")),
            ],
        ),
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=50, verbose_name="Titulo")),
                ("release_date", models.DateField(verbose_name="Fecha lanzamiento")),
                (
                    "front_page",
                    models.ImageField(upload_to="front_page", verbose_name="Portada"),
                ),
                ("visits", models.PositiveIntegerField(verbose_name="Visitas")),
                (
                    "authors",
                    models.ManyToManyField(to="author.author", verbose_name="Autor"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="book.category",
                        verbose_name="Categoría",
                    ),
                ),
            ],
        ),
    ]
