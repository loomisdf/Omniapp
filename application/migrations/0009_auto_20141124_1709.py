# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_application_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='photo',
            field=models.ImageField(upload_to='img'),
            preserve_default=True,
        ),
    ]
