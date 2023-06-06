# Generated by Django 4.2.1 on 2023-06-05 23:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ultracomp', '0007_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentmodel',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='ultracomp.commentmodel'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='laptop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='laptop_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
