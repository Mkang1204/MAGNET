# Generated by Django 2.0.1 on 2018-02-06 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magnet_v030', '0004_auto_20180206_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='authors',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='full_title',
            field=models.TextField(blank=True),
        ),
    ]