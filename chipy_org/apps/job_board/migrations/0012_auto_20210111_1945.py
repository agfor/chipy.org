# Generated by Django 2.2.17 on 2021-01-11 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0011_remove_jobpost_days_to_expire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='description',
            field=models.CharField(help_text="5000 Character Limit. Create a new paragraph by pressing 'Enter' twice.", max_length=5000),
        ),
    ]