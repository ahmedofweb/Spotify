# Generated by Django 4.2.6 on 2023-10-27 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('asosiyApp', '0002_alter_albom_rasm_alter_qoshiq_davomiylik_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Izoh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matn', models.CharField(max_length=150)),
                ('sana', models.DateTimeField(auto_now_add=True)),
                ('kino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiyApp.qoshiq')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
