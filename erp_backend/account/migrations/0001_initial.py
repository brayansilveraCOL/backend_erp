# Generated by Django 3.1 on 2021-04-11 04:50

from django.db import migrations, models
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='Create Date')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Modified Date')),
                ('UniqueCode', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Code Unique Generate')),
                ('CodeInternal', models.CharField(max_length=10, unique=True, verbose_name='Code Unique Internal')),
                ('date_payment_initial', models.DateField(verbose_name='Date Payment Initial')),
                ('date_payment_final', models.DateField(verbose_name='Date Payment Final')),
                ('average_pay_rate', models.DecimalField(decimal_places=2, help_text='Average Pay Rate', max_digits=6, verbose_name='Average Pay Rate')),
                ('balance_due', models.DecimalField(decimal_places=2, help_text='Balance Due Account', max_digits=6, null=True, verbose_name='Balance Due')),
                ('status_account_internal', models.CharField(choices=[('CA', 'Cancel'), ('AC', 'Active'), ('DE', 'Debts')], max_length=50, verbose_name='Status account')),
            ],
            options={
                'verbose_name': 'Base Model',
                'verbose_name_plural': 'Base Model',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalAccount',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='State')),
                ('create_date', models.DateField(blank=True, editable=False, verbose_name='Create Date')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Modified Date')),
                ('UniqueCode', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Code Unique Generate')),
                ('CodeInternal', models.CharField(db_index=True, max_length=10, verbose_name='Code Unique Internal')),
                ('date_payment_initial', models.DateField(verbose_name='Date Payment Initial')),
                ('date_payment_final', models.DateField(verbose_name='Date Payment Final')),
                ('average_pay_rate', models.DecimalField(decimal_places=2, help_text='Average Pay Rate', max_digits=6, verbose_name='Average Pay Rate')),
                ('balance_due', models.DecimalField(decimal_places=2, help_text='Balance Due Account', max_digits=6, null=True, verbose_name='Balance Due')),
                ('status_account_internal', models.CharField(choices=[('CA', 'Cancel'), ('AC', 'Active'), ('DE', 'Debts')], max_length=50, verbose_name='Status account')),
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
    ]
