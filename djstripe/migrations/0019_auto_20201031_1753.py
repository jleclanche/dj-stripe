# Generated by Django 3.1.2 on 2020-10-31 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0018_customer_default_balance_delinquent"),
    ]

    operations = [
        migrations.RemoveField(model_name="account", name="branding_icon"),
        migrations.RemoveField(model_name="account", name="branding_logo"),
    ]
