# Generated by Django 3.2.6 on 2022-01-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0016_rename_num_of_rzs_extendeduser_num_of_lifeline'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='extra_time',
            field=models.IntegerField(default=0),
        ),
    ]
