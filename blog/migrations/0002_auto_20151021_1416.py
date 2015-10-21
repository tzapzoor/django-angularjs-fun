# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='date_published',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='date_updated',
            new_name='updated_at',
        ),
    ]
