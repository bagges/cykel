# Generated by Django 2.2.4 on 2019-10-24 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bikesharing", "0014_auto_20191024_1611"),
    ]

    operations = [
        migrations.AddField(
            model_name="location",
            name="accuracy",
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
