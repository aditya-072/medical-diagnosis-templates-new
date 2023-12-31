# Generated by Django 4.2.1 on 2023-07-25 04:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patient_app', '0005_delete_constant_patient_med_test1_delete_receipt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Med_test2_5_report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reffered_by', models.CharField(max_length=200, null=True)),
                ('validated_by', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('lab_no', models.IntegerField(null=True)),
                ('t1', models.TextField(null=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='med_test2_5_report', to='patient_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Med_test2_4_report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reffered_by', models.CharField(max_length=200, null=True)),
                ('validated_by', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('lab_no', models.IntegerField(null=True)),
                ('t1', models.TextField(null=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='med_test2_4_report', to='patient_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Med_test2_3_report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reffered_by', models.CharField(max_length=200, null=True)),
                ('validated_by', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('lab_no', models.IntegerField(null=True)),
                ('t1', models.TextField(null=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='med_test2_3_report', to='patient_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Med_test2_2_report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reffered_by', models.CharField(max_length=200, null=True)),
                ('validated_by', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('lab_no', models.IntegerField(null=True)),
                ('t1', models.TextField(null=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='med_test2_2_report', to='patient_app.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Med_test2_1_report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reffered_by', models.CharField(max_length=200, null=True)),
                ('validated_by', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateField(default=django.utils.timezone.now)),
                ('lab_no', models.IntegerField(null=True)),
                ('t1', models.TextField(null=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='med_test2_1_report', to='patient_app.patient')),
            ],
        ),
    ]
