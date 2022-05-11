# Generated by Django 4.0.3 on 2022-05-10 22:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0023_reviewer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='reviewerOne',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewerOne', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='conference',
            name='reviewerThree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewerThree', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='conference',
            name='reviewerTwo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewerTwo', to=settings.AUTH_USER_MODEL),
        ),
    ]
