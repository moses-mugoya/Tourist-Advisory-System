# Generated by Django 2.1.4 on 2019-02-10 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourism', '0003_auto_20190210_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='activity',
            field=models.CharField(default='Sight seeing', max_length=250),
        ),
    ]
