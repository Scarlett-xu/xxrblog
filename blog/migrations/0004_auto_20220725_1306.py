# Generated by Django 3.2.14 on 2022-07-25 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220725_1302'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='articles',
        #     name='id',
        #     field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
        #     preserve_default=False,
        # ),
        migrations.AlterField(
            model_name='articles',
            name='pid',
            field=models.IntegerField(default=1),
        ),
    ]
