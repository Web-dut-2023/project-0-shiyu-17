# Generated by Django 3.1 on 2020-08-20 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0027_auto_20200820_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='listing',
            name='initial_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.bid'),
        ),
    ]