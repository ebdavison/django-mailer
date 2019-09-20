# Generated by Django 3.0a1 on 2019-09-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailer', '0003_messagelog_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(1, 'high'), (2, 'medium'), (3, 'low'), (4, 'deferred')], default=2),
        ),
        migrations.AlterField(
            model_name='messagelog',
            name='priority',
            field=models.PositiveSmallIntegerField(choices=[(1, 'high'), (2, 'medium'), (3, 'low'), (4, 'deferred')], db_index=True),
        ),
    ]
