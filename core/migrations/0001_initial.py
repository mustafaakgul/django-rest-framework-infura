# Generated by Django 4.0.5 on 2022-06-05 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(max_length=200)),
                ('body_id', models.CharField(max_length=100)),
                ('jsonrpc', models.CharField(max_length=100)),
            ],
        ),
    ]
