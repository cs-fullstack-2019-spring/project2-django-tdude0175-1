# Generated by Django 2.0.6 on 2019-03-13 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WikiApp', '0003_auto_20190313_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesidecontentmodel',
            name='ArticleLink',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='WikiApp.WikiArticleModel'),
        ),
        migrations.AlterField(
            model_name='wikiarticlemodel',
            name='User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='WikiApp.WikiEditorModel'),
        ),
        migrations.AlterField(
            model_name='wikieditormodel',
            name='Accountlink',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]