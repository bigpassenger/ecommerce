# Generated by Django 4.2.3 on 2024-09-20 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_mobile_company_product_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ('name',), 'verbose_name': 'company', 'verbose_name_plural': 'companies'},
        ),
    ]
