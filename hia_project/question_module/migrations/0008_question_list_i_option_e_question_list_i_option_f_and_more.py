# Generated by Django 5.0.4 on 2024-05-05 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_module', '0007_question_option_e'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='list_i_option_e',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='list_i_option_f',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='list_i_option_g',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='list_i_option_h',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]