# Generated by Django 2.0 on 2017-12-11 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0002_auto_20171125_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
