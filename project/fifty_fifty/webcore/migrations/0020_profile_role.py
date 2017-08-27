
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webcore', '0019_auto_20170430_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Mentee', 'Mentee'), ('Mentor', 'Mentor')], max_length=15, null=True),
        ),
    ]
