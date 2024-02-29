# Generated by Django 4.2.6 on 2023-10-19 16:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('guid', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('test_mode', models.IntegerField(choices=[(1, 'En línea'), (2, 'Fuera de línea'), (3, 'Desarrollo')], verbose_name='Mode')),
                ('is_mobile', models.BooleanField(default=False, verbose_name='Is mobile')),
                ('browser', models.CharField(blank=True, max_length=30, null=True, verbose_name='Browser')),
                ('operating_system', models.CharField(blank=True, max_length=30, null=True, verbose_name='Operating system')),
                ('birthdate', models.CharField(max_length=4, verbose_name='Birthdate')),
                ('sex', models.CharField(choices=[('Male', 'Hombre'), ('Female', 'Mujer'), ('Other', 'No me identifico con estas opciones'), ('N/A', 'Prefiero no responder')], max_length=10, verbose_name='Sex')),
                ('education', models.CharField(choices=[('School', 'Escuela'), ('First Cycle', 'Educación media básica (3º de liceo terminado o similar)'), ('Secondary education', 'Educación media superior (6º de liceo terminado o similar)'), ('Tertiary education', 'Educación terciaria (tecnicatura, diplomatura o grado universitario)'), ('Other', 'No me identifico con estas opciones'), ('N/A', 'Prefiero no responder')], max_length=30, verbose_name='Education')),
                ('preferred_language', models.CharField(choices=[('AR_RP', 'Argentina - Rioplatense'), ('AR_CO', 'Argentina - Cordobés'), ('AR_CY', 'Argentina - Cuyano'), ('AR_GU', 'Argentina - Nor-oriental-guarani'), ('AR_LSA', 'Argentina - LSA'), ('UY_RP', 'Uruguay - Rioplatense'), ('UY_LSU', 'Uruguay - LSU'), ('Other', 'No me identifico con estas opciones'), ('N/A', 'Prefiero no responder')], default='N/A', max_length=20, verbose_name='Preferred language')),
            ],
            options={
                'verbose_name': 'Form',
                'verbose_name_plural': 'Forms',
            },
        ),
        migrations.CreateModel(
            name='Stimulus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=50, verbose_name='Term')),
                ('is_word', models.BooleanField(default=True, verbose_name='Is word')),
            ],
            options={
                'verbose_name': 'Stimulus',
                'verbose_name_plural': 'Stimuli',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decision', models.BooleanField(blank=True, null=True, verbose_name='Decision')),
                ('rt', models.IntegerField(blank=True, null=True, verbose_name='Response time')),
                ('te', models.IntegerField(blank=True, null=True, verbose_name='Time elapsed')),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='decisions.form', verbose_name='Form')),
                ('stimulus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='decisions.stimulus', verbose_name='Stimulus')),
            ],
            options={
                'verbose_name': 'Reply',
                'verbose_name_plural': 'Replies',
                'unique_together': {('form', 'stimulus')},
            },
        ),
    ]