# Generated by Django 3.2 on 2023-09-19 15:46

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
                ('created_at', models.DateField(auto_now_add=True)),
                ('brand_name', models.CharField(max_length=255)),
                ('brand_description', models.TextField(max_length=255)),
                ('brand_country', models.CharField(blank=True, max_length=255, null=True)),
                ('brand_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DEACTIVE', 'DEACTIVE')], default='DEACTIVE', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('category_name', models.CharField(max_length=255)),
                ('category_description', models.TextField(max_length=255)),
                ('category_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DEACTIVE', 'DEACTIVE')], default='DEACTIVE', max_length=8)),
                ('category_brands', models.ManyToManyField(to='App.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_phone', models.CharField(max_length=10)),
                ('customer_email', models.CharField(blank=True, max_length=255, null=True)),
                ('customer_address', models.TextField(blank=True, max_length=255, null=True)),
                ('customer_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DEACTIVE', 'DEACTIVE')], default='DEACTIVE', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.TimeField(auto_now_add=True)),
                ('product_name', models.CharField(max_length=255)),
                ('product_buying_price', models.PositiveIntegerField()),
                ('product_selling_price', models.PositiveIntegerField()),
                ('product_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DEACTIVE', 'DEACTIVE')], default='DEACTIVE', max_length=8)),
                ('product_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.brand')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.category')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('supplier_name', models.CharField(max_length=255, unique=True)),
                ('supplier_company', models.CharField(max_length=255)),
                ('supplier_phone', models.CharField(max_length=10)),
                ('supplier_email', models.CharField(max_length=255)),
                ('supplier_address', models.TextField(max_length=255)),
                ('supplier_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DEACTIVE', 'DEACTIVE')], default='DEACTIVE', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='SystemUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('system_user_first_name', models.CharField(max_length=255)),
                ('system_user_last_name', models.CharField(max_length=255)),
                ('system_user_username', models.CharField(max_length=255, unique=True)),
                ('system_user_phone', models.CharField(max_length=10)),
                ('system_user_email', models.CharField(max_length=255, unique=True)),
                ('system_user_nic_number', models.CharField(max_length=20)),
                ('system_user_password', models.CharField(max_length=255)),
                ('system_user_type', models.CharField(choices=[('ADMIN', 'ADMIN'), ('USER', 'USER')], default='USER', max_length=5)),
                ('system_user_status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('DEACTIVE', 'DEACTIVE')], default='DEACTIVE', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('product_quantity', models.PositiveIntegerField()),
                ('product_unit_price', models.PositiveIntegerField()),
                ('product_total_price', models.PositiveIntegerField()),
                ('product_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.product')),
            ],
        ),
        migrations.CreateModel(
            name='SupplierBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('sub_total', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(blank=True, null=True)),
                ('net_total', models.PositiveIntegerField()),
                ('payment_method', models.CharField(choices=[('CASH', 'CASH'), ('CHQ', 'CHQ'), ('CREDIT', 'CREDIT')], default='CREDIT', max_length=6)),
                ('payment_status', models.CharField(choices=[('PAID', 'PAID'), ('NOT PAID', 'NOT PAID')], default='NOT PAID', max_length=8)),
                ('invoices', models.ManyToManyField(to='App.SupplierInvoice')),
                ('supplier_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.supplier')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.supplier'),
        ),
        migrations.CreateModel(
            name='CustomerInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('product_quantity', models.PositiveIntegerField()),
                ('product_unit_price', models.PositiveIntegerField()),
                ('product_total_price', models.PositiveIntegerField()),
                ('product_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.product')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('sub_total', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField(blank=True, null=True)),
                ('net_total', models.PositiveIntegerField()),
                ('payment_method', models.CharField(choices=[('CASH', 'CASH'), ('CHQ', 'CHQ'), ('CREDIT', 'CREDIT')], default='CREDIT', max_length=6)),
                ('payment_status', models.CharField(choices=[('PAID', 'PAID'), ('NOT PAID', 'NOT PAID')], default='NOT PAID', max_length=8)),
                ('customer_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.customer')),
                ('invoices', models.ManyToManyField(to='App.CustomerInvoice')),
            ],
        ),
    ]
