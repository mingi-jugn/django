# Generated by Django 3.2.6 on 2021-08-28 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0003_remove_webtoon_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='webtoon',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
