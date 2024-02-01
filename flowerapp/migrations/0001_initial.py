# Generated by Django 5.0 on 2023-12-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('sname', models.CharField(max_length=250)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='garden')),
            ],
        ),
    ]
