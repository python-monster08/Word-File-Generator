# Generated by Django 5.0.4 on 2024-04-29 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='level_of_defficulty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='question_module.defficultylevel'),
        ),
    ]