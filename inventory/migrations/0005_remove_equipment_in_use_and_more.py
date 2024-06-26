# Generated by Django 5.0.3 on 2024-03-21 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_equipment_in_use_alter_brand_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='in_use',
        ),
        migrations.AlterField(
            model_name='user_equipment',
            name='equipment',
            field=models.ForeignKey(limit_choices_to={'user_equipment__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.equipment', verbose_name='equipo'),
        ),
    ]
