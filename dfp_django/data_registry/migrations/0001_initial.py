# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataFromPapers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('paper_cite', models.CharField(max_length=1000)),
                ('paper_doi', models.CharField(max_length=200)),
                ('paper_url', models.CharField(max_length=200)),
                ('study_doi', models.CharField(max_length=200)),
                ('data_id', models.CharField(max_length=200)),
                ('data_url', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
