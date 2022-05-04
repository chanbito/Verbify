# Generated by Django 3.2.5 on 2022-05-04 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.DateTimeField(auto_now_add=True)),
                ('mensagem', models.TextField(max_length=500, verbose_name='mensagem')),
                ('token', models.TextField(max_length=90, verbose_name='token')),
                ('is_human', models.BooleanField(default=False, verbose_name='humano')),
            ],
            options={
                'verbose_name': 'mensagem',
                'verbose_name_plural': 'mensagens',
                'ordering': ['id'],
            },
        ),
    ]