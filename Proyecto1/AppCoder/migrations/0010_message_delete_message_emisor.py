# Generated by Django 4.0.4 on 2022-06-03 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0009_message_emisor_delete_message_delete_posteos'),
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateTimeField(default=None)),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.user')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCoder.post')),
            ],
        ),
        migrations.DeleteModel(
            name='message_emisor',
        ),
    ]