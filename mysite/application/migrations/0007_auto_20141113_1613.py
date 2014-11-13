# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_supported_platform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supported_platform',
            old_name='platform',
            new_name='title',
        ),
    ]
