# Generated by Django 2.2.1 on 2019-06-02 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0008_auto_20190603_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='approval',
            field=models.BooleanField(default=False),
        ),
    ]
