# Generated by Django 4.1.3 on 2022-11-08 22:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rename_chain_product_chain_fk_alter_product_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 11, 8, 22, 12, 47, 423567, tzinfo=datetime.timezone.utc), verbose_name='relise date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]
