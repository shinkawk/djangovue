# Generated by Django 3.0 on 2019-12-12 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191212_1757'),
        ('recipes', '0003_auto_20191212_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrecipe',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.User'),
            preserve_default=False,
        ),
    ]
