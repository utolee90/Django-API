# Generated by Django 3.1 on 2020-09-16 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0004_scores_reg_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='reg_user',
        ),
    ]