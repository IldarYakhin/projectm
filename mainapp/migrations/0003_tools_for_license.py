# Generated by Django 3.1.3 on 2020-11-28 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='tools_for_license',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
