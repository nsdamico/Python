# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-27 18:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('hired_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('add_by', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ManyToManyField(related_name='owner_wish', to='wishlist.User')),
                ('uploder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_uplod', to='wishlist.User')),
            ],
        ),
    ]