# Generated by Django 4.2.4 on 2023-10-13 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0004_delete_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='Address',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='Contact_number',
        ),
    ]
