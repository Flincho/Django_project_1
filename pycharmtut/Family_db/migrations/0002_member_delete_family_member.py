# Generated by Django 4.0.4 on 2022-05-15 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Family_db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('birthday', models.DateField()),
                ('kinship_deg', models.IntegerField()),
                ('icecream_flavor', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='Family_member',
        ),
    ]
