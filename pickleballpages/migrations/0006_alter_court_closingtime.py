# Generated by Django 4.1.2 on 2022-12-09 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pickleballpages', '0005_remove_court_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='closingtime',
            field=models.CharField(max_length=30, null=True),
        ),
    ]