# Generated by Django 3.0.8 on 2020-10-29 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='Example: ifeeze25@gmail.com', max_length=254)),
                ('subject', models.CharField(help_text='Subject of discussion', max_length=100)),
                ('message', models.TextField(max_length=10000)),
            ],
        ),
    ]
