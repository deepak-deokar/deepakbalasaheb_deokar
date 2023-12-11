# Generated by Django 4.2.6 on 2023-12-10 09:05

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):
    dependencies = [
        ("Contacts", "0003_contact_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="country",
            field=models.CharField(default="United States", max_length=100),
        ),
        migrations.AddField(
            model_name="contact",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True, max_length=128, null=True, region=None
            ),
        ),
    ]