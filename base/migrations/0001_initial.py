# Generated by Django 5.0 on 2023-12-24 05:28

import base.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.CharField(default=base.models.generate_ulid, max_length=128, primary_key=True, serialize=False)),
            ],
        ),
    ]