# Generated by Django 5.2.4 on 2025-07-13 15:19

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_alter_blogpost_content'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='tags',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
