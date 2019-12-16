# Generated by Django 3.0 on 2019-12-16 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191216_1129'),
        ('recipes', '0004_userrecipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrecipe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='users.User'),
        ),
    ]
