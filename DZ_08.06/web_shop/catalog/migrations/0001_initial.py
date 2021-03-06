# Generated by Django 4.0.5 on 2022-06-12 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quality', models.CharField(choices=[('PR', 'Premium'), ('HI', 'Hight'), ('ME', 'Medium'), ('ST', 'Standart'), ('LO', 'Low')], max_length=50)),
                ('products_type', models.CharField(choices=[('B', 'Books'), ('C', 'Clothes'), ('T', 'Toys')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cost', models.PositiveIntegerField()),
                ('availability', models.BooleanField()),
                ('photo', models.FileField(blank=True, null=True, upload_to='uploads/photo_models')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalog.brand')),
            ],
        ),
    ]
