# Generated by Django 3.0.8 on 2020-07-26 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20200726_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(default='msathyakumar9@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
