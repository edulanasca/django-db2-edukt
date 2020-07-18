# Generated by Django 3.0.8 on 2020-07-17 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0006_auto_20200717_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='school',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='subscription.School'),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='subscription.University'),
        ),
    ]
