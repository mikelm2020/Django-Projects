# Generated by Django 4.1.1 on 2022-09-17 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("author", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="author",
            options={"verbose_name": "Autor", "verbose_name_plural": "Autores"},
        ),
    ]
