# Generated by Django 4.1.1 on 2022-09-17 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Reader",
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
                ("age", models.PositiveIntegerField(default=18, verbose_name="Edad")),
            ],
        ),
        migrations.CreateModel(
            name="Loan",
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
                ("loan_date", models.DateField(verbose_name="Fecha prestámo")),
                (
                    "return_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Fecha devolución"
                    ),
                ),
                ("returned", models.BooleanField(verbose_name="Devuelto")),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="book.book",
                        verbose_name="Libro",
                    ),
                ),
                (
                    "reader",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="loan.reader",
                        verbose_name="Lector",
                    ),
                ),
            ],
        ),
    ]
