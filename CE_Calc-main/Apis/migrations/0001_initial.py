# Generated by Django 4.0.1 on 2022-07-19 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('state', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'TimeStamp',
                'verbose_name_plural': 'TimeStamps',
            },
        ),
        migrations.CreateModel(
            name='RecentUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('capacity_percent', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('timestamp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Apis.timestamp')),
            ],
            options={
                'verbose_name': 'recent_usage',
                'verbose_name_plural': 'recent_usages',
            },
        ),
        migrations.CreateModel(
            name='BatteryUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.TimeField()),
                ('energy_percent', models.IntegerField()),
                ('energy', models.IntegerField()),
                ('timestamp', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Apis.timestamp')),
            ],
            options={
                'verbose_name': 'battery_usage',
                'verbose_name_plural': 'battery_usages',
            },
        ),
    ]