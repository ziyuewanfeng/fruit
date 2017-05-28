# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20170528_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell_user_fruit',
            name='picture',
            field=models.CharField(default=b'abt1.jpg', max_length=200),
        ),
    ]
