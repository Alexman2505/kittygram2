# Generated by Django 3.2.3 on 2023-04-06 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0005_auto_20230407_0140'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='cat',
            name='unique_name_owner',
        ),
        migrations.AddConstraint(
            model_name='cat',
            constraint=models.UniqueConstraint(fields=('name', 'owner'), name='unique_name_owner'),
        ),
    ]
