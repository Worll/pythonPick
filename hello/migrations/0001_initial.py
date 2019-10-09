# Generated by Django 2.2.6 on 2019-10-08 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('commentText', models.CharField(max_length=255)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('authorID', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('pictureUrl', models.CharField(max_length=100)),
                ('pictureID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('numberOfComments', models.IntegerField()),
                ('authorID', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('numberOfPhotos', models.IntegerField()),
            ],
        ),
    ]