# Generated by Django 2.1.2 on 2019-07-19 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lines', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linemodel',
            name='id',
            field=models.CharField(default='line_2019719163931b7f0309e', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='routemodel',
            name='id',
            field=models.CharField(default='route_2019719163931cad3b93a', max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]