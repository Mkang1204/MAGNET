# Generated by Django 2.0.1 on 2018-01-28 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magnet_v030', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cluster',
            options={'ordering': []},
        ),
        migrations.AddField(
            model_name='cluster',
            name='cluster_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cluster',
            name='cluster_description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]