# Generated by Django 4.0 on 2021-12-12 20:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.date(2021, 12, 12)),
        ),
    ]
