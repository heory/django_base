# Generated by Django 2.2.19 on 2021-03-28 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeopleInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
                ('gender', models.SmallIntegerField(choices=[(1, 'male'), (2, 'female')], default=1)),
                ('description', models.CharField(max_length=100, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.BookInfo')),
            ],
            options={
                'db_table': 'peopleinfo',
            },
        ),
    ]
