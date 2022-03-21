# Generated by Django 4.0.2 on 2022-02-20 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opponent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Dialog opponent')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selfDialogs', to=settings.AUTH_USER_MODEL, verbose_name='Dialog owner')),
            ],
        ),
        migrations.AlterModelManagers(
            name='message',
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False, verbose_name='Read'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to=settings.AUTH_USER_MODEL, verbose_name='Author'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='text',
            field=models.TextField(default=1, verbose_name='Message text'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.AddField(
            model_name='message',
            name='dialog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat.dialog', verbose_name='Dialog'),
            preserve_default=False,
        ),
    ]