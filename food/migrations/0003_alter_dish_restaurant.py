# Generated by Django 5.1.6 on 2025-02-24 13:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="restaurant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dishes",
                to="food.restaurant",
            ),
        ),
    ]
