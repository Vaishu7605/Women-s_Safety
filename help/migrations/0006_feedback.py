# Generated by Django 5.0 on 2023-12-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0005_remove_clients_address_remove_clients_contact_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('feedback', models.TextField()),
            ],
        ),
    ]
