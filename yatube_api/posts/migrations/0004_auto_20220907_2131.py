# Generated by Django 2.2.16 on 2022-09-07 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220907_2123'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='follower',
            new_name='user',
        ),
    ]