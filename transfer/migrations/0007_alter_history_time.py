# Generated by Django 4.1.6 on 2023-05-04 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0006_alter_history_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 4, 9, 15, 17, 683720, tzinfo=datetime.timezone.utc)),
        ),
    ]
