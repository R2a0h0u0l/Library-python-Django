# Generated by Django 3.2.9 on 2022-01-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=200)),
                ('book_id', models.FloatField(max_length=10)),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]
