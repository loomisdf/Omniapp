# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20141113_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='photo',
            field=models.ImageField(default='img.url', upload_to='media'),
            preserve_default=False,
        ),
    ]
