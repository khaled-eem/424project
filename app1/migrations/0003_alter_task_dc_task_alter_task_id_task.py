# Generated by Django 5.0.6 on 2024-05-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dc_task',
            field=models.CharField(max_length=364),
        ),
        migrations.AlterField(
            model_name='task',
            name='id_task',
            field=models.CharField(max_length=364),
        ),
    ]
