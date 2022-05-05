# Generated by Django 4.0.4 on 2022-05-05 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CVSS2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_score', models.CharField(max_length=200, verbose_name='Базовая метрика')),
                ('AV', models.CharField(max_length=200, verbose_name='Получение доступа')),
                ('AC', models.CharField(max_length=200, verbose_name='Сложность получение доступа')),
                ('AU', models.CharField(max_length=200, verbose_name='Показатель аутонтефикации')),
                ('C', models.CharField(max_length=200, verbose_name='Влияние на конфиденциальность')),
                ('I', models.CharField(max_length=200, verbose_name='Влияние на целостность')),
                ('A', models.CharField(max_length=200, verbose_name='Влияние на доступность')),
            ],
        ),
        migrations.CreateModel(
            name='CVSS3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_score', models.CharField(max_length=200, verbose_name='Базовая метрика')),
                ('time_score', models.CharField(max_length=300, verbose_name='Временная метрика')),
                ('AV', models.CharField(max_length=200, verbose_name='Получение доступа')),
                ('AC', models.CharField(max_length=200, verbose_name='Сложность получение доступа')),
                ('PR', models.CharField(max_length=200, verbose_name='Взаимодействие с пользователем')),
                ('UI', models.CharField(max_length=200, verbose_name='Требуемые привилегии')),
                ('S', models.CharField(max_length=200, verbose_name='Объем')),
                ('C', models.CharField(max_length=200, verbose_name='Влияние на конфиденциальность')),
                ('I', models.CharField(max_length=200, verbose_name='Влияние на целостность')),
                ('A', models.CharField(max_length=200, verbose_name='Влияние на доступность')),
                ('E', models.CharField(max_length=200, verbose_name='Доступность эксплойда')),
                ('RL', models.CharField(max_length=200, verbose_name='Уровень исправления')),
                ('RC', models.CharField(max_length=200, verbose_name='Отчет о достоверности')),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название узла')),
            ],
        ),
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название уязвимости')),
                ('short_description', models.TextField(verbose_name='Краткое описание')),
                ('description', models.TextField(verbose_name='Описание')),
                ('edit', models.TextField(verbose_name='Как исправить')),
                ('cvss2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.cvss2')),
                ('cvss3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.cvss3')),
            ],
        ),
        migrations.CreateModel(
            name='Group_vulnerability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.IntegerField(verbose_name='Порт')),
                ('tcp_udp', models.CharField(choices=[('tcp', 'TCP'), ('udp', 'UDP')], default='tcp', max_length=3)),
                ('name_protocol', models.CharField(max_length=200, verbose_name='Название протокола')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.node')),
                ('vulnerability', models.ManyToManyField(to='report.vulnerability')),
            ],
        ),
    ]
