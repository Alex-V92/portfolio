# Generated by Django 4.0 on 2021-12-12 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_project_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_blog',
            name='description',
            field=models.TextField(default='default'),
        ),
        migrations.AlterField(
            model_name='project_blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 12, 22, 43, 31, 260104)),
        ),
    ]