# Generated by Django 3.2.14 on 2022-07-24 08:11

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewcount', models.IntegerField(default=1)),
                ('title', models.CharField(default='title', max_length=300)),
                ('pid', models.IntegerField(default=1)),
                ('describtion', models.CharField(default='describtion', max_length=300)),
                ('tag', models.CharField(default='tag', max_length=100)),
                ('content', mdeditor.fields.MDTextField()),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
