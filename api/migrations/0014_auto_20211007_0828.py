# Generated by Django 3.2.8 on 2021-10-07 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_pickups_dis_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispatches',
            name='date_created',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pickups',
            name='p_arv_date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pickups',
            name='p_dep_date',
            field=models.CharField(max_length=200),
        ),
    ]