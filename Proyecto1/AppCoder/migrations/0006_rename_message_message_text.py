# Generated by Django 4.0.4 on 2022-06-03 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0005_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='text',
        ),
    ]
