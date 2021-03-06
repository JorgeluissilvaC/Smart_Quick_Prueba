# Generated by Django 3.0.6 on 2020-05-20 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('client_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='client.Clients')),
            ],
        ),
        migrations.CreateModel(
            name='BillsProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bill.Bills')),
                ('product_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Products')),
            ],
        ),
    ]
