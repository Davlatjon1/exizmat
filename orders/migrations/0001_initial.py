# Generated by Django 3.1.5 on 2021-01-05 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=60, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('postal_code', models.CharField(max_length=30, verbose_name='Почтовый индекс')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('tel_number', models.CharField(max_length=13, null=True, verbose_name='Номер телефона')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачено')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.product')),
            ],
        ),
    ]
