# Generated by Django 3.1 on 2021-04-11 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('billing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalaccount',
            name='bill',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='billing.bill'),
        ),
    ]
