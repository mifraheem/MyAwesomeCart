# Generated by Django 4.2.1 on 2023-06-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogpost',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=5000)),
                ('head0', models.CharField(max_length=90)),
                ('head1', models.CharField(max_length=90)),
                ('head2', models.CharField(max_length=90)),
                ('pub_date', models.DateField()),
                ('thumbnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]