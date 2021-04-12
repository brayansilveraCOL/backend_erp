# Generated by Django 3.1 on 2021-04-11 04:50

import django.core.validators
from django.db import migrations, models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Create Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('address', models.CharField(blank=True, max_length=25, null=True, verbose_name='Address User')),
            ],
            options={
                'verbose_name': 'Base Model',
                'verbose_name_plural': 'Base Model',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Create Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('address', models.CharField(blank=True, max_length=25, null=True, verbose_name='Address User')),
                ('full_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Full Name Contact')),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Not Valid Phone Number', regex='\\+?1?\\d{9,15}$')], verbose_name='Phone Number')),
                ('title_contact', models.CharField(blank=True, max_length=5, null=True, verbose_name='Title Contact')),
            ],
            options={
                'verbose_name': 'Base Model',
                'verbose_name_plural': 'Base Model',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalAddress',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Create Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('address', models.CharField(blank=True, max_length=25, null=True, verbose_name='Address User')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Base Model',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalContact',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Create Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('address', models.CharField(blank=True, max_length=25, null=True, verbose_name='Address User')),
                ('full_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Full Name Contact')),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Not Valid Phone Number', regex='\\+?1?\\d{9,15}$')], verbose_name='Phone Number')),
                ('title_contact', models.CharField(blank=True, max_length=5, null=True, verbose_name='Title Contact')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Base Model',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPhone',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Create Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Not Valid Phone Number', regex='\\+?1?\\d{9,15}$')], verbose_name='Phone Number')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Base Model',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Create Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Not Valid Phone Number', regex='\\+?1?\\d{9,15}$')], verbose_name='Phone Number')),
            ],
            options={
                'verbose_name': 'Base Model',
                'verbose_name_plural': 'Base Model',
                'abstract': False,
            },
        ),
    ]