# Generated by Django 4.2.1 on 2023-11-12 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_category_id_alter_product_store_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-id']},
        ),
    ]
