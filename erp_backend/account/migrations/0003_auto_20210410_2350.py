# Generated by Django 3.1 on 2021-04-11 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0002_historicalaccount_bill'),
        ('billing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list_price', '0002_auto_20210410_2350'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalaccount',
            name='customer',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalaccount',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalaccount',
            name='quotas',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='list_price.typeplan', verbose_name='Number of Quotas Plan'),
        ),
        migrations.AddField(
            model_name='historicalaccount',
            name='userInternal',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='bill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.bill'),
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='account',
            name='quotas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list_price.typeplan', verbose_name='Number of Quotas Plan'),
        ),
        migrations.AddField(
            model_name='account',
            name='userInternal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_internal', to=settings.AUTH_USER_MODEL),
        ),
    ]
