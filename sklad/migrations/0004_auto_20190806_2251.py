# Generated by Django 2.2.3 on 2019-08-06 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0003_colorandprice_co'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colorandprice',
            name='BL',
        ),
        migrations.RemoveField(
            model_name='colorandprice',
            name='BR',
        ),
        migrations.RemoveField(
            model_name='colorandprice',
            name='GR',
        ),
        migrations.RemoveField(
            model_name='colorandprice',
            name='OL',
        ),
        migrations.RemoveField(
            model_name='colorandprice',
            name='RED',
        ),
        migrations.RemoveField(
            model_name='colorandprice',
            name='YE',
        ),
        migrations.RemoveField(
            model_name='colorandprice',
            name='co',
        ),
        migrations.AddField(
            model_name='colorandprice',
            name='cena',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='colorandprice',
            name='color',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
