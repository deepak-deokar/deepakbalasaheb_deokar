# Generated by Django 4.2.6 on 2023-12-12 00:35

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("Contacts", "0004_contact_country_contact_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="country",
            field=models.CharField(default="Country", max_length=100),
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                default="1234567890", max_length=128, null=True, region=None
            ),
        ),
    ]