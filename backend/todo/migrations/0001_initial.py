# Generated by Django 4.1.1 on 2023-10-25 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('success', models.BooleanField(default=False)),
                ('errorMessage', models.CharField(max_length=1024, null=True)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2048)),
                ('status', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
    ]
