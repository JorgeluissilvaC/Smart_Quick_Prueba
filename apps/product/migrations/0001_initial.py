# Generated by Django 3.0.6 on 2020-05-20 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('attribute1', models.CharField(max_length=50)),
                ('attribute2', models.CharField(max_length=50)),
                ('attribute3', models.CharField(max_length=50)),
                ('attribute4', models.CharField(max_length=50)),
            ],
        ),
    ]
