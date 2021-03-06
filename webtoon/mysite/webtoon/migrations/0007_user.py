# Generated by Django 3.2.6 on 2021-09-01 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtoon', '0006_mcomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='사용자명')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
                ('registered_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'db_table': 'test_user',
            },
        ),
    ]
