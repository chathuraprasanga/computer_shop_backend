# Generated by Django 4.2.4 on 2023-09-02 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ComputerShopApp', '0002_alter_buyer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='user_status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DECATIVE', 'DEACTIVE')], default='DEACTIVE', max_length=10),
        ),
    ]