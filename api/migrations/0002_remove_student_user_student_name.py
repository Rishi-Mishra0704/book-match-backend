# Generated by Django 5.0 on 2023-12-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='user',
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
