# Generated by Django 5.1.6 on 2025-02-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('amount_of_calories', models.DecimalField(decimal_places=1, max_digits=7)),
            ],
        ),
    ]
