# Generated by Django 4.2.7 on 2024-02-13 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hodApp', '0006_subject'),
        ('staffApp', '0002_staff_notification_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff_Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_from_date', models.CharField(max_length=20)),
                ('leave_to_date', models.CharField(max_length=20)),
                ('leave_days', models.IntegerField()),
                ('leave_message', models.TextField()),
                ('leave_status', models.IntegerField(default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hodApp.staff')),
            ],
        ),
    ]
