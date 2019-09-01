# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-01 10:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=40, null=True)),
                ('time_comment', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-time_comment'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='photos/')),
                ('image_name', models.CharField(max_length=40, null=True)),
                ('image_caption', models.TextField(null=True)),
                ('likes', models.IntegerField(default=0)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-date_uploaded'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(null=True, upload_to='profiles/')),
                ('user_bio', models.TextField()),
                ('last_update', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-last_update'],
            },
        ),
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instagram.Profile'),
        ),
        migrations.AddField(
            model_name='comments',
            name='Image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instagram.Image'),
        ),
    ]
