# Generated by Django 3.2.14 on 2023-07-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20230515_1020'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='passages',
            name='Surface_img',
            field=models.CharField(default='https://xxrblog.oss-cn-nanjing.aliyuncs.com/Snipaste_2023-01-16_14-59-04.png', max_length=100),
        )
    ]
