# Generated by Django 4.1.7 on 2023-02-18 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teste1', '0006_remove_produto_nome_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='indicador_oferta',
            field=models.BooleanField(default=False),
        ),
    ]
