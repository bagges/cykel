# Generated by Django 2.2.3 on 2019-07-26 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bikesharing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="rent",
            name="end_station",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="rent_end_station",
                to="bikesharing.Station",
            ),
        ),
        migrations.AddField(
            model_name="rent",
            name="start_station",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="rent_start_station",
                to="bikesharing.Station",
            ),
        ),
    ]
