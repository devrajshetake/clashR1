# Generated by Django 3.2.6 on 2021-10-31 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userresponse',
            name='selected_option',
            field=models.IntegerField(blank=True, choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')], null=True),
        ),
    ]
