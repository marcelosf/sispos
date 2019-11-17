# Generated by Django 2.2.6 on 2019-11-17 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0004_report_aluno'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'verbose_name': 'relatório', 'verbose_name_plural': 'relatórios'},
        ),
        migrations.CreateModel(
            name='ParecerOrientadorMestrado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s1_desempenho', models.CharField(max_length=2048)),
                ('s1_projeto', models.CharField(max_length=2048)),
                ('s1_outras_atividades', models.CharField(max_length=2048)),
                ('s2_desempenho', models.CharField(max_length=2048)),
                ('s2_metodologia', models.CharField(max_length=2048)),
                ('s2_abordagem', models.CharField(max_length=2048)),
                ('s2_outras_atividades', models.CharField(max_length=2048)),
                ('s3_resultados', models.CharField(max_length=2048)),
                ('s3_perspectivas', models.CharField(max_length=2048)),
                ('s3_resumo', models.CharField(max_length=2048)),
                ('s3_outras_atividades', models.CharField(max_length=2048)),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Report')),
            ],
        ),
    ]
