# Generated by Django 4.0 on 2022-03-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=150)),
                ('type', models.CharField(choices=[('Kg', 'Kgs'), ('Tonnes', 'Tonnes')], max_length=20)),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
