# Generated by Django 2.1.3 on 2018-12-14 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_skill_order_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skill',
            new_name='Interest',
        ),
    ]

    atomic = False