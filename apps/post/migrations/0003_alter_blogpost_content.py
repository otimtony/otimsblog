# Generated by Django 5.2.4 on 2025-07-12 22:15

import markdownx.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_category_rename_added_by_blogpost_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
    ]
