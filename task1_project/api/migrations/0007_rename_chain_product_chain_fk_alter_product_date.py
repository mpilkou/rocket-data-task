# Generated by Django 4.1.3 on 2022-11-08 14:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_product_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='chain',
            new_name='chain_fk',
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 8, 14, 30, 11, 77503, tzinfo=datetime.timezone.utc), verbose_name='relise date'),
        ),
    ]
