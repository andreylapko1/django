# Generated by Django 5.1.6 on 2025-02-12 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('in_progress', 'In progress'), ('pending', 'Pending'), ('blocked', 'Blocked'), ('done', 'Done')], default='new', max_length=100),
        ),
    ]
