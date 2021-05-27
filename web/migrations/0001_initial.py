# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-15 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_string', models.CharField(max_length=255, verbose_name='Reference String')),
                ('akamai_response', models.TextField(verbose_name='Akamai Response')),
            ],
        ),
    ]