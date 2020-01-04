# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-01-04 20:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='picture_folder/')),
                ('image_name', models.CharField(max_length=25)),
                ('image_caption', models.CharField(blank=True, max_length=400)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('image_likes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('profile', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='instagram.Profile')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
    ]