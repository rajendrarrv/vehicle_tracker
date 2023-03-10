# Generated by Django 4.1.6 on 2023-02-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=20)),
                ('email_text', models.CharField(max_length=20, unique=True)),
                ('mobile_no_text', models.CharField(max_length=12, unique=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
