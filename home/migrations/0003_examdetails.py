# Generated by Django 4.0.3 on 2022-05-29 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamDetails',
            fields=[
                ('Eid', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Date', models.DateField()),
            ],
        ),
    ]
