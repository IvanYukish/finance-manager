# Generated by Django 3.1.3 on 2021-02-02 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210113_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='debtor_name',
            field=models.CharField(max_length=100, unique=True, verbose_name="Ім'я"),
        ),
    ]
