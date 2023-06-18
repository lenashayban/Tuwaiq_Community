# Generated by Django 4.2.2 on 2023-06-16 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0008_alter_bootcamp_end_date_alter_contactus_descripton"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bootcamp",
            name="end_date",
            field=models.DateField(
                default=datetime.datetime(
                    2023, 7, 16, 18, 23, 15, 300931, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="contactus",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]