# Generated by Django 4.0.3 on 2022-05-09 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_rename_aurhor_article_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='user',
        ),
    ]
