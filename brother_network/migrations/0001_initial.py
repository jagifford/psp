# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brother',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.CharField(primary_key=True, serialize=False, unique=True, max_length=2)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('admin', models.OneToOneField(to='brother_network.Brother')),
                ('brothers', models.ManyToManyField(related_name='Brothers', to='brother_network.Brother')),
                ('chapter', models.ForeignKey(to='brother_network.Chapter')),
                ('events', models.ManyToManyField(to='brother_network.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=1000)),
                ('submit_date', models.DateTimeField()),
                ('submitter', models.ForeignKey(to='brother_network.Brother')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='posts',
            field=models.ManyToManyField(to='brother_network.Post'),
        ),
        migrations.AddField(
            model_name='brother',
            name='chapter',
            field=models.ForeignKey(default='DB', to='brother_network.Chapter'),
        ),
        migrations.AddField(
            model_name='brother',
            name='groups',
            field=models.ManyToManyField(to='brother_network.Group'),
        ),
    ]
