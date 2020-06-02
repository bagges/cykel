# Generated by Django 2.2.4 on 2019-10-24 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bikesharing", "0013_auto_20191024_1437"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="bike",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="bikesharing.Bike",
            ),
        ),
        migrations.CreateModel(
            name="LocationTracker",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "lora_tracker_id",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "last_reported",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "battery_voltage",
                    models.FloatField(blank=True, default=None, null=True),
                ),
                (
                    "tracker_type",
                    models.CharField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "bike",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="bikesharing.Bike",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="location",
            name="tracker",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="bikesharing.LocationTracker",
            ),
        ),
    ]
