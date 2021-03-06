from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=100)),
                ('artist_genre', models.CharField(max_length=50)),
                ('artist_email', models.CharField(max_length=100)),
                ('artist_location', models.CharField(max_length=100)),
                ('artist_social', models.CharField(max_length=100)),
                ('artist_website', models.CharField(max_length=100)),
                ('artist_bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_company', models.CharField(
                    default='Enter Company Representative', max_length=100)),
                ('detail_membership', models.CharField(
                    default='Enter Membership Group', max_length=100)),
                ('detail_picture', models.ImageField(
                    blank=True, null=True, upload_to='artist/picture/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                             related_name='details', to='musicsite.Artist')),
            ],
        ),
    ]
