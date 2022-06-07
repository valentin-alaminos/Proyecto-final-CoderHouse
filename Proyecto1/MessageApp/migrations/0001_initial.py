# Generated by Django 4.0.4 on 2022-06-03 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('emisor', models.CharField(max_length=255)),
                ('receptor', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=None)),
            ],
        ),
    ]