# Generated by Django 3.0 on 2019-12-12 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191212_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresource',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='users.User'),
        ),
    ]