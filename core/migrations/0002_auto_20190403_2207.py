# Generated by Django 2.2 on 2019-04-03 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='age',
            field=models.IntegerField(default=13),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='first_name',
            field=models.CharField(default='John', max_length=200),
            preserve_default=False,
        ),
    ]
