# Generated by Django 2.2.10 on 2021-08-27 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20210827_2055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created_at',)},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='level',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply_to',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='tree_id',
        ),
    ]
