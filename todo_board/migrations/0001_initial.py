# Generated by Django 4.0.1 on 2022-01-09 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_list',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('pcode', models.CharField(max_length=4)),
                ('user_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
                ('is_complete', models.BooleanField()),
                ('date', models.DateField()),
            ],
        ),
    ]
