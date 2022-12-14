# Generated by Django 4.1.2 on 2022-11-16 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courtname', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to='photos')),
                ('courtaddress', models.CharField(max_length=300)),
                ('numberofcourts', models.IntegerField(default=0)),
                ('courtofficiators', models.BooleanField(default=False)),
                ('lights', models.BooleanField(default=False)),
                ('closingtime', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'Courts',
            },
        ),
    ]
