# Generated by Django 4.0.1 on 2023-02-11 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('bn_name', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Upazila',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('bn_name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood_bank.division')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('bn_name', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9)),
                ('url', models.URLField()),
                ('division_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blood_bank.division')),
            ],
        ),
        migrations.CreateModel(
            name='Blood_doner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=5)),
                ('contact_no', models.CharField(max_length=30)),
                ('address_line_1', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=100)),
                ('data_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=15)),
                ('last_donation_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('district', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blood_bank.district')),
                ('division', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blood_bank.division')),
                ('upazila', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blood_bank.upazila')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blood_bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('contact_no', models.CharField(max_length=50)),
                ('address_line_1', models.CharField(max_length=500)),
                ('zip_code', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(max_length=100)),
                ('district', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blood_bank.district')),
                ('division', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blood_bank.division')),
                ('upazila', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blood_bank.upazila')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]