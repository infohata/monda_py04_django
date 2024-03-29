# Generated by Django 5.0 on 2024-03-21 12:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_support', '0003_alter_ticket_subject'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='sender_email',
            field=models.EmailField(blank=True, db_index=True, max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='sender_name',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='full name'),
        ),
        migrations.CreateModel(
            name='TicketMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='full name')),
                ('sender_email', models.EmailField(blank=True, db_index=True, max_length=254, null=True, verbose_name='email')),
                ('recipient_name', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='full name')),
                ('recipient_email', models.EmailField(blank=True, db_index=True, max_length=254, null=True, verbose_name='email')),
                ('sent_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='sent at')),
                ('mail_sent', models.BooleanField(default=False, verbose_name='email sent')),
                ('is_read', models.BooleanField(default=False, verbose_name='is read')),
                ('recipient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_ticket_messages', to=settings.AUTH_USER_MODEL, verbose_name='recipient')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_ticket_messages', to=settings.AUTH_USER_MODEL, verbose_name='sender')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_support.ticket', verbose_name='ticket')),
            ],
            options={
                'verbose_name': 'ticket message',
                'verbose_name_plural': 'ticket messages',
            },
        ),
    ]
