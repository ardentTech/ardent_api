# Generated by Django 2.0.7 on 2018-07-30 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0004_auto_20180718_1632'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='@todo', max_length=128, verbose_name='name'),
        ),
    ]
