# Generated by Django 4.2 on 2024-07-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchhistory',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]
