# Generated by Django 5.0.6 on 2024-06-09 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0002_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
    ]
