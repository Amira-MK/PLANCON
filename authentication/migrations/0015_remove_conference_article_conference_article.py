# Generated by Django 4.0.3 on 2022-05-09 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_conference_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='article',
        ),
        migrations.AddField(
            model_name='conference',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.article'),
        ),
    ]
