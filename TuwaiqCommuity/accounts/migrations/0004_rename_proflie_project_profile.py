# Generated by Django 4.2.2 on 2023-06-21 05:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='proflie',
            new_name='profile',
        ),
    ]
