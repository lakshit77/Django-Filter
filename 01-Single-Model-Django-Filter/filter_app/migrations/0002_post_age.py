# Generated by Django 4.1.7 on 2023-05-01 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filter_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='age',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
