# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-25 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0047_auto_20170314_0042'),
    ]

    operations = [
        migrations.AddField(
            model_name='footerinfo',
            name='email_signup',
            field=models.TextField(blank=True, help_text='you can enter code here for an email signup', null=True),
        ),
    ]