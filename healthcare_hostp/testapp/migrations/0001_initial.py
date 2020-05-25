# Generated by Django 3.0.6 on 2020-05-25 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=25)),
                ('pincode', models.IntegerField()),
                ('nick_name', models.CharField(max_length=20)),
            ],
        ),
    ]