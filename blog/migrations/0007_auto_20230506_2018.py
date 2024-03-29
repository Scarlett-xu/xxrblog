# Generated by Django 3.2.14 on 2023-05-06 12:18

from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20230504_1523'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='articles',
        #     name='id',
        # ),
        # migrations.RemoveField(
        #     model_name='articles',
        #     name='tagid',
        # ),
        # migrations.RemoveField(
        #     model_name='tags',
        #     name='id',
        # ),
        # migrations.AlterField(
        #     model_name='articles',
        #     name='pid',
        #     field=models.AutoField(primary_key=True, serialize=False),
        # ),
        # migrations.AlterField(
        #     model_name='tags',
        #     name='tagid',
        #     field=models.AutoField(primary_key=True, serialize=False),
        # ),
        migrations.CreateModel(
            name='Passages',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('viewcount', models.IntegerField(default=1)),
                ('title', models.CharField(default='title', max_length=300)),
                ('describtion', models.CharField(default='describtion', max_length=300)),
                ('content', mdeditor.fields.MDTextField()),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('tagid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tags')),
            ],
        ),
    ]
