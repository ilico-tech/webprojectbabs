# Generated by Django 4.1.7 on 2023-04-02 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autoexpress', '0016_remove_voiture_user_alter_voiture_boitevitesse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voiture',
            name='proprio',
        ),
    ]
