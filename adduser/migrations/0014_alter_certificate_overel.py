# Generated by Django 5.0.4 on 2024-05-02 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adduser', '0013_alter_certificate_title_alter_userinfo_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='overel',
            field=models.CharField(choices=[('C1', 'C1'), ('B2', 'B2')], max_length=2, verbose_name='Overel'),
        ),
    ]
