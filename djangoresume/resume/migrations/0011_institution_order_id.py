# Generated by Django 2.1.3 on 2018-12-29 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_auto_20181214_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='order_id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
