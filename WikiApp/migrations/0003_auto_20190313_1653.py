# Generated by Django 2.0.6 on 2019-03-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0002_auto_20190313_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesidecontentmodel',
            name='SidePicture',
            field=models.ImageField(blank=True, null=True, upload_to='Side_Content_Images'),
        ),
        migrations.AlterField(
            model_name='wikiarticlemodel',
            name='Body',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='wikiarticlemodel',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='Article_Images'),
        ),
        migrations.AlterField(
            model_name='wikieditormodel',
            name='ProfilePicture',
            field=models.ImageField(blank=True, null=True, upload_to='Profile_Pictures'),
        ),
    ]
