# Generated by Django 2.2.4 on 2019-09-02 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190901_0820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product_catagory',
            old_name='Catagory_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='topping',
            old_name='topping_name',
            new_name='name',
        ),
    ]
