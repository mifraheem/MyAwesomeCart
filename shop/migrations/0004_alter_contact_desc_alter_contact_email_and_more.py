# Generated by Django 4.2.1 on 2023-05-20 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.CharField(default=' ', max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default=' ', max_length=70),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default=' ', max_length=70),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=' ', max_length=70),
        ),
    ]
