# Generated by Django 5.0.1 on 2024-05-11 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_task', models.CharField(max_length=64)),
                ('n_task', models.CharField(max_length=64)),
                ('dc_task', models.CharField(max_length=64)),
                ('dr_task', models.CharField(max_length=64)),
            ],
        ),
    ]
