# Generated by Django 5.1.1 on 2024-10-08 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('zip_code', models.CharField(max_length=120)),
            ],
        ),
    ]
