# Generated by Django 2.2.16 on 2020-09-19 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20200919_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='telephone',
            field=models.CharField(max_length=11),
        ),
    ]
