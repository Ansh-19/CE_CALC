# Generated by Django 4.0.1 on 2022-08-06 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Apis', '0004_alter_batteryusage_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batteryusage',
            name='timestamp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bu', to='Apis.timestamp'),
        ),
        migrations.AlterField(
            model_name='recentusage',
            name='timestamp',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ru', to='Apis.timestamp'),
        ),
    ]