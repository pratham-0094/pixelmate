# Generated by Django 3.1.12 on 2022-10-25 10:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import pixelmate.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectOnGoing',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Url', models.CharField(max_length=50)),
                ('Technology', djongo.models.fields.ArrayField(model_container=pixelmate.models.Tech, model_form_class=pixelmate.models.TechForm)),
                ('Username', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pixelmate.signup')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectCompleted',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Description', models.CharField(max_length=50)),
                ('CreatedDate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('CompletedDate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Url', models.CharField(max_length=50)),
                ('Technology', djongo.models.fields.ArrayField(model_container=pixelmate.models.Tech, model_form_class=pixelmate.models.TechForm)),
                ('Username', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pixelmate.signup')),
            ],
        ),
    ]
