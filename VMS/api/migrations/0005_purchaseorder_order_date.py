# Generated by Django 5.0.4 on 2024-05-04 05:01

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_purchaseorder_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorder',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
