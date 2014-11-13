# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20141113_0234'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
