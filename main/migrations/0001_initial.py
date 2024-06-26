# Generated by Django 5.0.3 on 2024-03-29 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
                ('sector', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
