# Generated by Django 3.0.2 on 2020-02-11 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhaseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase_type', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('productOwner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('teamID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOpened', models.DateField()),
                ('dateClosed', models.DateField(blank=True, null=True)),
                ('tag', models.CharField(max_length=50)),
                ('severity', models.CharField(choices=[('Minor', 'Minor'), ('Major', 'Major')], max_length=25)),
                ('url', models.URLField()),
                ('projectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restAPI.Project')),
                ('whereFound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restAPI.PhaseType')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('projectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restAPI.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOpened', models.DateField()),
                ('dateClosed', models.DateField(blank=True, null=True)),
                ('tag', models.CharField(max_length=50)),
                ('severity', models.CharField(choices=[('Minor', 'Minor'), ('Major', 'Major')], max_length=25)),
                ('url', models.URLField()),
                ('projectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restAPI.Project')),
                ('whereFound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restAPI.PhaseType')),
            ],
        ),
    ]
