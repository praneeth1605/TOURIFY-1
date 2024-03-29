# Generated by Django 5.0.1 on 2024-02-02 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Tourist_table',
            },
        ),
        migrations.CreateModel(
            name='TouristRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('confirmpassword', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'TouristRegister_table',
            },
        ),
        migrations.CreateModel(
            name='Userfeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hotel', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('cleanliness', models.CharField(max_length=100)),
                ('service', models.CharField(max_length=100)),
                ('comfort', models.CharField(max_length=100)),
                ('amenities', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=100)),
                ('comments', models.TextField()),
            ],
            options={
                'db_table': 'Feedback_table',
            },
        ),
    ]
