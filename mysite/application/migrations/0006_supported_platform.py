# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supported_Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=200)),
                ('application', models.ForeignKey(to='application.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
