# Generated by Django 4.2 on 2023-04-05 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='autor',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livro',
            name='nome',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
