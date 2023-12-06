# Generated by Django 3.1 on 2020-08-13 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20200812_0806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='owner',
        ),
        migrations.AlterField(
            model_name='bid',
            name='price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
    ]