# Generated by Django 4.2 on 2023-04-05 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0002_livro_autor_livro_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='data_cadastro',
            field=models.DateField(auto_now_add=True),
        ),
    ]
