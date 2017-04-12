# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20170412_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(related_name='studentuser', to=settings.AUTH_USER_MODEL),
        ),
    ]
