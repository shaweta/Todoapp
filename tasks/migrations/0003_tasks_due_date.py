# Generated by Django 5.0 on 2023-12-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_tasks_options_alter_tasks_created_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='due_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
