# Generated by Django 4.1.7 on 2023-04-03 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoexpress', '0019_voiture_cartegrise_voiture_email_voiture_nom_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='cartegrise',
            field=models.FileField(blank=True, default=False, null=True, upload_to=' '),
        ),
    ]
