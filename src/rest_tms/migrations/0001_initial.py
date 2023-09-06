# Generated by Django 4.2.5 on 2023-09-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('count', models.PositiveIntegerField()),
                ('discription', models.TextField(blank=True, null=True)),
                ('visible', models.BooleanField(default=True)),
            ],
        ),
    ]
