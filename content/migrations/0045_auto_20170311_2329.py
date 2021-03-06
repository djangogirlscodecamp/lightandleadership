# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-11 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0044_eduprogram_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='donatesection',
            name='paypal_button',
            field=models.TextField(blank=True, help_text='enter the paypal code if you want it in this section.', null=True),
        ),
        migrations.AlterField(
            model_name='donatesection',
            name='order',
            field=models.PositiveIntegerField(help_text='Enter a number. 1 will be at the top of each section(section order: aboutus, donate, club, paypal'),
        ),
        migrations.AlterField(
            model_name='eduprogram',
            name='video',
            field=models.BooleanField(default=False, help_text='check here if you want this section to be full width'),
        ),
        migrations.AlterField(
            model_name='home',
            name='img',
            field=models.ImageField(blank=True, help_text='Image is optional. If there is no image, this section will be full width', null=True, upload_to='aboutus'),
        ),
    ]
