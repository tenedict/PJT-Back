# Generated by Django 4.1.3 on 2022-12-01 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0006_alter_members_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="members",
            name="project",
            field=models.IntegerField(null=True),
        ),
    ]