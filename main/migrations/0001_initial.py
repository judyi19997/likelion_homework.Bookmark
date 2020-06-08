# Generated by Django 3.0.7 on 2020-06-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookmarkModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=20)),
                ('site_url', models.URLField(max_length=1000)),
            ],
        ),
    ]
