# Generated by Django 3.1 on 2021-06-27 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacao', '0008_auto_20210627_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaEspecial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especial', models.BooleanField()),
                ('nome_deficiencia', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='pessoa',
            name='especial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='aplicacao.pessoaespecial'),
        ),
    ]
