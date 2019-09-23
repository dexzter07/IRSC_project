# Generated by Django 2.2.4 on 2019-09-23 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
                ('available_date', models.DateTimeField()),
                ('Hotel_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discount', models.BooleanField(default=False)),
            ],
        ),
    ]
