# Generated by Django 2.2 on 2019-05-24 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20190524_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='group',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='inviter',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='person',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.DeleteModel(
            name='Membership',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
