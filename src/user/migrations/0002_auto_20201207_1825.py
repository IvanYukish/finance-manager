# Generated by Django 3.1.3 on 2020-12-07 18:25

from django.db import migrations, models
import user.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, db_index=True, max_length=20, null=True, validators=[user.validators.CustomPhoneNumberValidator()], verbose_name='Номер Телефону'),
        ),
    ]
