# Generated by Django 4.0.4 on 2022-06-06 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0018_rename_image_img_rename_img_img_imagen_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='img',
        ),
        migrations.AddField(
            model_name='post',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
