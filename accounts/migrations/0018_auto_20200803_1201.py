# Generated by Django 3.0.8 on 2020-08-03 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20200803_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='academicfee',
            field=models.FloatField(default=50000),
        ),
    ]