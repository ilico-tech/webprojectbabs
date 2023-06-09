# Generated by Django 4.1.7 on 2023-04-04 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autoexpress', '0020_alter_voiture_cartegrise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='annee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='telephone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voiture',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
