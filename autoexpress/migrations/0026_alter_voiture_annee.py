# Generated by Django 4.1.7 on 2023-04-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoexpress', '0025_remove_voiture_datereser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='annee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]