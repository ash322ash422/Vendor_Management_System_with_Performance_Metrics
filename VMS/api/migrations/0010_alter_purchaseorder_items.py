# Generated by Django 5.0.4 on 2024-05-04 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_purchaseorder_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='items',
            field=models.JSONField(default=dict),
        ),
    ]
