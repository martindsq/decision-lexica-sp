# Generated by Django 4.2.6 on 2023-10-19 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decisions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stimulus',
            name='file_name',
            field=models.CharField(default='hello.png', max_length=50, verbose_name='Filename'),
            preserve_default=False,
        ),
    ]
