# Generated by Django 4.1.7 on 2023-02-16 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao_produto', models.TextField()),
                ('preco_normal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco_oferta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('indicador_oferta', models.BooleanField()),
            ],
        ),
    ]