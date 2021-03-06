# Generated by Django 4.0.3 on 2022-03-13 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('project_img', models.ImageField(upload_to='project/%Y/%m/%d')),
                ('project_url', models.TextField(blank=True, null=True)),
                ('github_url', models.TextField()),
            ],
        ),
    ]
