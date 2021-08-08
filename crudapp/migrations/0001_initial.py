# Generated by Django 3.1.7 on 2021-08-08 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField(default=0)),
                ('ename', models.CharField(max_length=10)),
                ('ecity', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'myemployees',
            },
        ),
    ]
