# Generated by Django 2.2 on 2019-04-16 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_aboutus_contacts_deliveryandpayment_exchangeandreturn_howtouse_logowithphones_socialnetwork_support'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logowithphones',
            name='logo',
            field=models.URLField(blank=True, null=True),
        ),
    ]