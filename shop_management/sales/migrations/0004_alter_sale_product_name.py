# Generated by Django 4.0 on 2022-03-14 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_type'),
        ('sales', '0003_alter_sale_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='product_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
