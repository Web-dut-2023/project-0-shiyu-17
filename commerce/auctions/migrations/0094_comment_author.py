# Generated by Django 3.1 on 2020-08-31 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0093_auto_20200831_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(default='billy', max_length=100),
            preserve_default=False,
        ),
    ]