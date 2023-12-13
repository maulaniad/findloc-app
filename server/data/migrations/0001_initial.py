# Generated by Django 4.2.8 on 2023-12-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=75)),
            ],
            options={
                'db_table': 'USER',
            },
        ),
    ]
