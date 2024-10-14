# Generated by Django 5.1.1 on 2024-10-14 19:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField(blank=True, null=True)),
                ('tags', models.TextField(blank=True, help_text='Use commas to separate tags', null=True)),
                ('make_public', models.BooleanField(blank=True, default=False, null=True)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
