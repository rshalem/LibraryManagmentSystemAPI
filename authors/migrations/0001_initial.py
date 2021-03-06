# Generated by Django 3.2.3 on 2021-05-22 16:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('author_name', models.CharField(max_length=255, unique=True)),
                ('author_registered', models.DateTimeField(auto_now_add=True)),
                ('bio', models.TextField()),
            ],
            options={
                'ordering': ['author_name'],
            },
        ),
    ]
