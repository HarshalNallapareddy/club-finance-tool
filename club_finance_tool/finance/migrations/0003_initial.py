# Generated by Django 4.2.4 on 2024-03-24 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('finance', '0002_remove_user_clubs_delete_club_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('club_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('is_institution', models.BooleanField()),
                ('manager_of', models.ManyToManyField(blank=True, related_name='managers', to='finance.club')),
                ('member_of', models.ManyToManyField(blank=True, related_name='members', to='finance.club')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('note', models.TextField()),
                ('club_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.club')),
            ],
        ),
    ]
