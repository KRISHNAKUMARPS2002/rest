# Generated by Django 4.2.7 on 2023-11-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('description', models.TextField()),
                ('date_enrolled', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
