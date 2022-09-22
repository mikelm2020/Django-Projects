# Generated by Django 4.1.1 on 2022-09-17 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
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
                ("name", models.CharField(max_length=50, verbose_name="Nombre")),
                ("last_name", models.CharField(max_length=50, verbose_name="Apellido")),
                (
                    "nationality",
                    models.CharField(max_length=30, verbose_name="Nacionalidad"),
                ),
                ("age", models.PositiveIntegerField(verbose_name="Edad")),
            ],
        ),
    ]