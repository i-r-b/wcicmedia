# Generated by Django 2.0.5 on 2018-09-12 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediarecipes', '0002_auto_20180912_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='number_contaminated',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='number_made',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='number_wasted',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='total_volume_made',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='volume_made',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
