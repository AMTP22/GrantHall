# Generated by Django 2.0.1 on 2018-04-18 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('cadet', models.BooleanField(default=False)),
                ('faculty', models.BooleanField(default=False)),
                ('stockPerson', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockQuantity', models.IntegerField()),
                ('foodName', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('espirationDate', models.DateField()),
                ('calories', models.IntegerField()),
                ('sodium', models.IntegerField()),
                ('sugar', models.IntegerField()),
                ('fat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiveDate', models.DateField()),
                ('paid', models.BooleanField(default=False)),
                ('orderType', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='granthall.Client')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='granthall.Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='granthall.Order')),
            ],
        ),
    ]
