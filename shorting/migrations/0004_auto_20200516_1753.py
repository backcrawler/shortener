# Generated by Django 2.2.12 on 2020-05-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorting', '0003_auto_20200420_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='url',
            field=models.CharField(max_length=400, unique=True),
        ),
    ]
