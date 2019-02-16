# Generated by Django 2.1.5 on 2019-02-16 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('received_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('amount', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='accounts.User')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('user', 'message')},
        ),
    ]