# Generated by Django 4.2.11 on 2024-04-15 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meetings", "0007_meeting_capacity_verified_meeting_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="meeting",
            name="status",
            field=models.CharField(
                choices=[("draft", "draft"), ("published", "published"), ("archived", "archived")],
                default="submitted",
                max_length=50,
            ),
        ),
    ]
