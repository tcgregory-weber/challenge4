# Generated by Django 4.1.9 on 2023-06-27 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PortfolioDatabase', '0004_hobby_imagelink_project_imagelink'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
