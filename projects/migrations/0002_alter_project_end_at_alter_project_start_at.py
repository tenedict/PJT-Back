# Generated by Django 4.1.3 on 2022-12-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="end_at",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="project",
            name="start_at",
            field=models.DateField(),
        ),
    ]
