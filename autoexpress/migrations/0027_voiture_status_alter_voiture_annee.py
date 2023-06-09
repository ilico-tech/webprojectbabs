# Generated by Django 4.1.7 on 2023-04-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoexpress', '0026_alter_voiture_annee'),
    ]

    operations = [
        migrations.AddField(
            model_name='voiture',
            name='status',
            field=models.CharField(choices=[('Disponible', 'Disponible'), ('Indisponible', 'Indisponible')], default=(('Disponible', 'Disponible'), ('Indisponible', 'Indisponible')), max_length=20),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='annee',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
