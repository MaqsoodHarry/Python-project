# Generated by Django 4.1.5 on 2023-11-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_icon', models.CharField(max_length=20)),
                ('model_title', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]
