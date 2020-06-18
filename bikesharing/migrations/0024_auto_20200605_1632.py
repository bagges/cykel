# Generated by Django 2.2.10 on 2020-06-05 14:32
# flake8: noqa

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bikesharing", "0023_auto_20200326_1857"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bikesharepreferences",
            name="gbfs_hide_bikes_after_location_report_hours",
            field=models.IntegerField(
                default=1,
                help_text="""
                Time period (in hours) after the vehicles will\n
                be hidden from GBFS, if there was no location report.\n
                Needs 'Gbfs hide bikes after location report silence' activated.""",
            ),
        ),
        migrations.AlterField(
            model_name="bikesharepreferences",
            name="gbfs_hide_bikes_after_location_report_silence",
            field=models.BooleanField(
                default=False,
                help_text="""
                If activated, vehicles will disappear from GBFS,\n
                if there was no location report in the configured time period.""",
            ),
        ),
        migrations.AlterField(
            model_name="location",
            name="internal",
            field=models.BooleanField(
                default=False,
                help_text="""Internal locations are not published to the enduser.\n
                They are useful for backup trackers
                with lower accuracy e.g. wifi trackers.""",
            ),
        ),
        migrations.AlterField(
            model_name="locationtracker",
            name="device_id",
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name="locationtracker",
            name="internal",
            field=models.BooleanField(
                default=False,
                help_text="""
                Internal trackers don't publish their locations to the enduser.\n
                They are useful for backup trackers
                with lower accuracy e.g. wifi trackers.""",
            ),
        ),
    ]