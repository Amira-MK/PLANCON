# Generated by Django 4.0.3 on 2022-05-09 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_article_soumission_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='aurhor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.author'),
        ),
    ]
