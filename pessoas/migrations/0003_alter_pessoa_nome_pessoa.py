# Generated by Django 4.1.4 on 2022-12-26 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_alter_pessoa_apelido_alter_pessoa_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='nome_pessoa',
            field=models.CharField(max_length=150),
        ),
    ]