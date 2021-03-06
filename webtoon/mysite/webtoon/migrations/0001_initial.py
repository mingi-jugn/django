# Generated by Django 3.2.6 on 2021-08-27 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webtoon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('support', models.CharField(max_length=20)),
                ('content', models.TextField(max_length=50, null=True)),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('make_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
