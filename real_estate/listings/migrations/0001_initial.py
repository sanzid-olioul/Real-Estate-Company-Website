# Generated by Django 4.0.4 on 2022-05-19 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('price', models.IntegerField()),
                ('number_of_bedrooms', models.IntegerField()),
                ('square_footage', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
