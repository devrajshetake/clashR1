# Generated by Django 3.2.6 on 2022-03-01 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0026_alter_extendeduser_tab'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='popLifelineModal',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='extendeduser',
            name='popRZModal',
            field=models.BooleanField(default=True),
        ),
    ]
