# Generated by Django 3.0.8 on 2020-07-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_new_model_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_model',
            name='small_int_field',
            field=models.IntegerField(default=True, null=True),
        ),
    ]