# Generated by Django 2.0.6 on 2019-03-13 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0005_auto_20190313_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesidecontentmodel',
            name='ArticleLink',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='WikiApp.WikiArticleModel'),
        ),
        migrations.AlterField(
            model_name='articlesidecontentmodel',
            name='SidePicture',
            field=models.ImageField(blank=True, null=True, upload_to='WikiApp/static/WikiApp/images/Side_Content_Images'),
        ),
        migrations.AlterField(
            model_name='wikiarticlemodel',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='WikiApp/static/WikiApp/images/Article_Images'),
        ),
        migrations.AlterField(
            model_name='wikieditormodel',
            name='ProfilePicture',
            field=models.ImageField(blank=True, null=True, upload_to='WikiApp/static/WikiApp/images/Profile_Pictures'),
        ),
    ]
