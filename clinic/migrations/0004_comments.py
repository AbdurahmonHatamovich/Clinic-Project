# Generated by Django 5.0.6 on 2024-05-16 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_alter_doctor_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('id',),
                'indexes': [models.Index(fields=['id'], name='clinic_comm_id_c40f26_idx')],
            },
        ),
    ]