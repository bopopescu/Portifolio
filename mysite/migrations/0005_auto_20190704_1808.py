# Generated by Django 2.2.1 on 2019-07-04 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20190704_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='celular',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='contato',
            name='telefone',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]
