# Generated by Django 4.2.1 on 2023-06-03 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_chead1_alter_blogpost_head2'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='chead0',
            field=models.CharField(default='', max_length=500),
        ),
    ]