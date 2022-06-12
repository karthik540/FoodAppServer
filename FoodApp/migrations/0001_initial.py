# Generated by Django 4.0.5 on 2022-06-12 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('foodId', models.AutoField(db_column='foodId', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('isAvailable', models.BooleanField()),
                ('imageUrl', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurantId', models.AutoField(db_column='restaurantId', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('rating', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tableId', models.IntegerField()),
                ('isOccupied', models.BooleanField()),
                ('sessionId', models.IntegerField(blank=True, null=True)),
                ('restaurantId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodApp.restaurant')),
            ],
            options={
                'unique_together': {('restaurantId', 'tableId')},
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.AutoField(db_column='orderId', primary_key=True, serialize=False)),
                ('sessionId', models.IntegerField()),
                ('foodQuantity', models.IntegerField()),
                ('foodID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodApp.food')),
                ('restaurantId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodApp.restaurant')),
                ('tableId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodApp.table')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='restaurantId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodApp.restaurant'),
        ),
    ]