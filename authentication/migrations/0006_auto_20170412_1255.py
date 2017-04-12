# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20170412_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='testscore',
            name='attempted',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(related_name='student', to=settings.AUTH_USER_MODEL),
        ),
    ]
