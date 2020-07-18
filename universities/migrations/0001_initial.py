# Generated by Django 3.0.8 on 2020-07-17 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_school', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_university', models.CharField(max_length=255)),
                ('initials', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UniversitySchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='universities.School')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='universities.University')),
            ],
        ),
    ]
