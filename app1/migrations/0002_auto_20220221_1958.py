# Generated by Django 3.2.11 on 2022-02-21 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tablemodel',
            old_name='dept_name',
            new_name='use0r',
        ),
        migrations.RemoveField(
            model_name='tablemodel',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='tablemodel',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='tablemodel',
            name='phone_num',
        ),
    ]