# Generated by Django 3.2.9 on 2021-12-08 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rememberwhenapi', '0002_rename_is_approved_fact_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='fact',
            name='category',
            field=models.ManyToManyField(related_name='Type', through='rememberwhenapi.FactCategory', to='rememberwhenapi.Category'),
        ),
    ]