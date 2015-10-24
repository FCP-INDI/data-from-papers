# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_registry', '0004_auto_20141116_2032'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Study',
            new_name='Studies',
        ),
    ]
