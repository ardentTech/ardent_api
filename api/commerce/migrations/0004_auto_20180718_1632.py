# Generated by Django 2.0.7 on 2018-07-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
        ('commerce', '0003_product_etsy_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-serial_number']},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ['id'], 'verbose_name_plural': 'Product Images'},
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='taxonomy.Tag'),
        ),
    ]
