# Generated by Django 5.0.4 on 2024-05-02 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adduser', '0003_alter_certificate_overel_alter_certificate_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='status',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='status',
            field=models.CharField(choices=[('uqimoqda', 'uqimoqda'), ('tugatgan', 'tugatgan')], default='uqimoqda', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='certificate',
            name='overel',
            field=models.CharField(choices=[('B2', 'B2'), ('C1', 'C1')], max_length=2, verbose_name='Overel'),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='title',
            field=models.CharField(choices=[('english', 'english'), ('nemesis', 'nemesis'), ('others', 'others')], max_length=300, verbose_name='Language'),
        ),
    ]
