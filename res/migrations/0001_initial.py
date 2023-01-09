# Generated by Django 4.0.3 on 2022-05-29 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0003_examdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rno', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('Eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.examdetails')),
                ('fid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.staff')),
            ],
        ),
    ]
