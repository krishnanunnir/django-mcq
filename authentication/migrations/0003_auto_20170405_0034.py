# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20170405_0029'),
        ('authentication', '0002_auto_20170405_0013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testscore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_score', models.IntegerField()),
                ('student', models.ForeignKey(to='authentication.Student')),
                ('test', models.ForeignKey(to='exam.Test')),
            ],
        ),
        migrations.RemoveField(
            model_name='testscores',
            name='student',
        ),
        migrations.RemoveField(
            model_name='testscores',
            name='test',
        ),
        migrations.DeleteModel(
            name='Testscores',
        ),
    ]
