# Generated by Django 3.1 on 2021-04-11 04:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('utils', '0001_initial'),
        ('inventorys', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcluster',
            name='Iva',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.iva'),
        ),
        migrations.AddField(
            model_name='productcluster',
            name='Product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='productcluster',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movement',
            name='cluster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventorys.cluster'),
        ),
        migrations.AddField(
            model_name='movement',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='movement',
            name='productCluster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventorys.productcluster'),
        ),
        migrations.AddField(
            model_name='movement',
            name='typeMovement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventorys.typemovement'),
        ),
        migrations.AddField(
            model_name='movement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaltypemovement',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalproductcluster',
            name='Cluster',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventorys.cluster'),
        ),
        migrations.AddField(
            model_name='historicalproductcluster',
            name='Iva',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='utils.iva'),
        ),
        migrations.AddField(
            model_name='historicalproductcluster',
            name='Product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.product'),
        ),
        migrations.AddField(
            model_name='historicalproductcluster',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalproductcluster',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalmovement',
            name='cluster',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventorys.cluster'),
        ),
        migrations.AddField(
            model_name='historicalmovement',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalmovement',
            name='product',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.product'),
        ),
        migrations.AddField(
            model_name='historicalmovement',
            name='productCluster',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventorys.productcluster'),
        ),
        migrations.AddField(
            model_name='historicalmovement',
            name='typeMovement',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='inventorys.typemovement'),
        ),
        migrations.AddField(
            model_name='historicalmovement',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalcluster',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]