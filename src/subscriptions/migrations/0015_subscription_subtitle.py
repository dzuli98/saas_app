# Generated by Django 5.0.12 on 2025-03-27 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0014_subscription_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='subtitle',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
