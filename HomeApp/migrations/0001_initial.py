# Generated by Django 3.2.16 on 2022-12-18 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('age', models.CharField(blank=True, max_length=400, null=True)),
                ('place', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
    ]
