# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('option_value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_no', models.IntegerField()),
                ('question_text', models.TextField()),
                ('answer', models.CharField(max_length=100)),
                ('options', models.ManyToManyField(to='exam.Option')),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher', models.CharField(max_length=30)),
                ('date_of_exam', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('questions', models.ManyToManyField(to='exam.Question')),
            ],
        ),
    ]
