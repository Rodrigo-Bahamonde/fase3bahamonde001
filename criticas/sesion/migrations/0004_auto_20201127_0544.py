# Generated by Django 2.2.3 on 2020-11-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sesion', '0003_perfil_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='tipo',
            field=models.CharField(choices=[('Admin', 'Admin'), ('User', 'User')], default='User', max_length=6),
        ),
    ]
