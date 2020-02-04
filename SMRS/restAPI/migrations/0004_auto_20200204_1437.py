# Generated by Django 3.0.2 on 2020-02-04 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0003_auto_20200204_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defect',
            name='dateClosed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='defect',
            name='severity',
            field=models.CharField(choices=[('Minor', 'Minor'), ('Major', 'Major')], max_length=25),
        ),
        migrations.AlterField(
            model_name='review',
            name='dateClosed',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='severity',
            field=models.CharField(choices=[('Minor', 'Minor'), ('Major', 'Major')], max_length=25),
        ),
    ]
