# Generated by Django 5.1.3 on 2024-12-08 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_rename_status_userprofile_status_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='status_role',
            new_name='status',
        ),
    ]