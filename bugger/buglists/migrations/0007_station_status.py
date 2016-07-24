# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buglists', '0006_auto_20160723_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='status',
            field=models.CharField(default='OPEN', max_length=5, verbose_name='status', choices=[(b'OPEN', 'OPEN'), (b'CLOSE', 'CLOSE')]),
            preserve_default=False,
        ),
    ]
