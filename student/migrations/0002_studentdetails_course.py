# Generated by Django 2.2 on 2021-05-09 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coursedetails', '0002_auto_20210507_2123'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='course',
            field=models.ManyToManyField(to='coursedetails.Coursedetails'),
        ),
    ]
