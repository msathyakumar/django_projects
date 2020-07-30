# Generated by Django 3.0.8 on 2020-07-30 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manf_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='framework',
            name='language',
            field=models.ManyToManyField(null=True, to='testapp.Language'),
        ),
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=30)),
                ('manf_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.manufacturer')),
            ],
        ),
    ]