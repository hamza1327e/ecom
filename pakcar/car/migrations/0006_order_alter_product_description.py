# Generated by Django 5.0.4 on 2024-04-28 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('postal_code', models.IntegerField(max_length=15)),
                ('description', models.CharField(max_length=255)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]