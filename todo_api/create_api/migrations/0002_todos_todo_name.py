# Generated by Django 5.1.1 on 2024-10-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='todo_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
