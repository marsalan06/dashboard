# Generated by Django 4.2 on 2023-05-07 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0006_business_user_alter_business_influencer'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='type_of_business',
            field=models.CharField(blank=True, choices=[('Influencer', 'Influencer'), ('Brand', 'Brand'), ('Agency', 'Agency'), ('Publisher', 'Publisher'), ('E-commerce', 'E-commerce'), ('SaaS', 'SaaS'), ('Media', 'Media'), ('Non-profit', 'Non-profit')], max_length=255, null=True),
        ),
    ]