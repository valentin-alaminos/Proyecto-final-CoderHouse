# Generated by Django 4.0.4 on 2022-06-03 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0010_message_delete_message_emisor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='receptor',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='emisor',
            new_name='usuario',
        ),
    ]
