# Generated by Django 4.2.11 on 2024-04-05 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meetings", "0004_topic_status_alter_meeting_live_stream"),
    ]

    operations = [
        migrations.AlterField(
            model_name="topic",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("submitted", "submitted"),
                    ("backlog", "backlog"),
                    ("coordinating", "coordinating"),
                    ("confirmed", "confirmed"),
                    ("declined", "declined"),
                    ("failed", "failed"),
                ],
                default="submitted",
                max_length=50,
                null=True,
            ),
        ),
    ]