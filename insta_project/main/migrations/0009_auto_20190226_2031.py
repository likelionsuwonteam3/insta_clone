# Generated by Django 2.1.5 on 2019-02-26 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_postlike'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likedpost',
        ),
        migrations.AddField(
            model_name='post',
            name='userlike',
            field=models.BooleanField(default=False),
        ),
    ]
