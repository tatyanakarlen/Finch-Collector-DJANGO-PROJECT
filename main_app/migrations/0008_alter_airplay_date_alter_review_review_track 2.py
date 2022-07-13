# Generated by Django 4.0.5 on 2022-07-12 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_rename_content_review_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airplay',
            name='date',
            field=models.DateField(verbose_name='Add airplay date'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review',
            field=models.TextField(max_length=1000),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.record')),
            ],
        ),
    ]
