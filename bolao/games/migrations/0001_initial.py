# Generated by Django 3.2.16 on 2022-11-09 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('teamId_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamId_1', to='teams.teams')),
                ('teamId_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamId_2', to='teams.teams')),
            ],
        ),
    ]
