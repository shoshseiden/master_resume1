# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 19:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master_resume1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customresume',
            name='contact_info',
        ),
        migrations.DeleteModel(
            name='ContactInformation',
        ),
    ]