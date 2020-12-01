# Generated by Django 3.1.3 on 2020-11-23 15:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Debts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено')),
                ('modified_at', models.DateTimeField(verbose_name='Модифіовано')),
                ('debtor_name', models.CharField(max_length=100)),
                ('mod', models.CharField(choices=[('+', 'Позичати (у когось)'), ('-', 'Позичити (комусь)')], max_length=1)),
                ('prise', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=500)),
                ('debt_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Користувач',
                'verbose_name_plural': 'Користувачі',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено')),
                ('modified_at', models.DateTimeField(verbose_name='Модифіовано')),
                ('prise', models.PositiveIntegerField()),
                ('description', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
