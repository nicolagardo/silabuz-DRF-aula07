# Generated by Django 4.1.4 on 2022-12-13 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="updated_at",
            field=models.DateField(auto_now=True),
        ),
    ]
