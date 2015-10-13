# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thumbsup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')]),
        ),
    ]
