# Generated by Django 3.2.7 on 2022-01-09 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rate',
            field=models.FloatField(),
        ),
    ]