# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_test_test_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='options',
        ),
        migrations.AddField(
            model_name='question',
            name='option_five',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_four',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_one',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_three',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_two',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_no',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='questions',
            field=models.ManyToManyField(to='exam.Question', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='teacher',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_title',
            field=models.CharField(default=b'Generic Test', max_length=100, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Option',
        ),
    ]
