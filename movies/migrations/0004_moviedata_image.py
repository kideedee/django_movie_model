# Generated by Django 4.2.4 on 2023-08-11 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_moviedata_typ'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedata',
            name='image',
            field=models.ImageField(default='images/default.jpeg', upload_to='images/'),
        ),
    ]
