# Generated by Django 4.0.5 on 2022-07-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_order', '0002_remove_cart_availability_remove_order_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('A', 'Awaiting'), ('CN', 'Confirmed'), ('P', 'Paid'), ('S', 'Sended'), ('СM', 'Complited')], max_length=50),
        ),
    ]
