# Generated by Django 3.2.6 on 2021-09-01 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0007_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]