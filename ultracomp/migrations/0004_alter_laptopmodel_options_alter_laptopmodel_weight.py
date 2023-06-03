# Generated by Django 4.2.1 on 2023-05-29 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ultracomp', '0003_alter_laptopmodel_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='laptopmodel',
            options={'verbose_name': 'laptop', 'verbose_name_plural': 'laptops'},
        ),
        migrations.AlterField(
            model_name='laptopmodel',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]