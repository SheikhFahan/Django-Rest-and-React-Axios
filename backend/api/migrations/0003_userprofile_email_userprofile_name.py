# Generated by Django 4.0.10 on 2023-08-19 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]