# Generated by Django 3.0.3 on 2020-02-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicusers', '0003_auto_20200220_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
