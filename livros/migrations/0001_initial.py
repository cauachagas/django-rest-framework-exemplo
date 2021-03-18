# Generated by Django 3.1.7 on 2021-03-18 02:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livros',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('ano', models.IntegerField()),
                ('estado', models.CharField(max_length=50)),
                ('paginas', models.IntegerField()),
                ('editora', models.CharField(max_length=255)),
                ('criado', models.DateField(auto_now_add=True)),
            ],
        ),
    ]