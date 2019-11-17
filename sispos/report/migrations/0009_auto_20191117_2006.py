# Generated by Django 2.2.6 on 2019-11-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0008_auto_20191117_0203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parecerorientadormestrado',
            options={'verbose_name': 'parecer do orientador - mestrado', 'verbose_name_plural': 'pareceres dos orientadores - mestrados'},
        ),
        migrations.AlterField(
            model_name='parecerorientadormestrado',
            name='s1_desempenho',
            field=models.TextField(max_length=2048, verbose_name='desempenho das disciplinas'),
        ),
        migrations.AlterField(
            model_name='parecerorientadormestrado',
            name='s1_outras_atividades',
            field=models.TextField(max_length=2048, verbose_name='outras atividades'),
        ),
        migrations.AlterField(
            model_name='parecerorientadormestrado',
            name='s1_projeto',
            field=models.TextField(max_length=2048, verbose_name='projeto de pesquisa'),
        ),
        migrations.AlterField(
            model_name='parecerorientadormestrado',
            name='s2_abordagem',
            field=models.TextField(max_length=2048, verbose_name='Abordagem do problema a ser investigado'),
        ),
        migrations.AlterField(
            model_name='parecerorientadormestrado',
            name='s2_desempenho',
            field=models.TextField(max_length=2048, verbose_name='desempenho das disciplinas'),
        ),
        migrations.AlterField(
            model_name='parecerorientadormestrado',
            name='s2_metodologia',
            field=models.TextField(max_length=2048, verbose_name='texto sobre a metodologia de trabalho'),
        ),
        migrations.AlterField(
            model_name='parecerorientadormestrado',
            name='s2_outras_atividades',
            field=models.TextField(max_length=2048, verbose_name='Outras Atividades'),
        ),
        migrations.AlterField(
            model_name='parecerorientadormestrado',
            name='s3_outras_atividades',
            field=models.TextField(max_length=2048, verbose_name='outras atividades'),
        ),
        migrations.AlterField(
            model_name='parecerorientadormestrado',
            name='s3_perspectivas',
            field=models.TextField(max_length=2048, verbose_name='perspectivas para a conclusão da dissertação'),
        ),
        migrations.AlterField(
            model_name='parecerorientadormestrado',
            name='s3_resultados',
            field=models.TextField(max_length=2048, verbose_name='resultados'),
        ),
        migrations.AlterField(
            model_name='parecerorientadormestrado',
            name='s3_resumo',
            field=models.TextField(max_length=2048, verbose_name='resumo expandido'),
        ),
    ]
