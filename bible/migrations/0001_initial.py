# Generated by Django 4.1.7 on 2023-04-05 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abbreviation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=3)),
                ('full_name', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='BibleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=3)),
                ('chapter', models.PositiveSmallIntegerField()),
                ('verse', models.PositiveSmallIntegerField()),
                ('contents', models.TextField()),
            ],
        ),
    ]