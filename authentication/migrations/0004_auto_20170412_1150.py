# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20170405_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
