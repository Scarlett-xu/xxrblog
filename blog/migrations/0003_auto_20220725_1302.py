# Generated by Django 3.2.14 on 2022-07-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_articles_surface_img'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='articles',
        #     name='id',
        # ),
        # migrations.AlterField(
        #     model_name='articles',
        #     name='pid',
        #     field=models.BigAutoField(primary_key=True, serialize=False),
        # ),
        migrations.AlterField(
            model_name='articles',
            name='surface_img',
            field=models.CharField(default='surface_img', max_length=100),
            preserve_default=False,
        ),
    ]
