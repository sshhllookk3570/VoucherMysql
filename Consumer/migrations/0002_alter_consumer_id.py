# Generated by Django 3.2 on 2021-04-08 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Consumer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
