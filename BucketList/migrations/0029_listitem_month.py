# Generated by Django 3.0.5 on 2020-05-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BucketList', '0028_announcements_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='month',
            field=models.TextField(blank=True, max_length=4, null=True),
        ),
    ]
