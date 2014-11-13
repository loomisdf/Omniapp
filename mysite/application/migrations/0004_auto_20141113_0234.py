# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='loggedIn',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
