# Generated by Django 3.0.3 on 2020-02-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicsite', '0004_auto_20200221_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='detail_picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]