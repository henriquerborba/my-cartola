# Generated by Django 4.1.4 on 2022-12-10 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minutes', models.IntegerField()),
                ('action', models.CharField(choices=[('goal', 'Goal'), ('assist', 'Assist'), ('yellow card', 'Yellow Card'), ('red card', 'Red Card')], max_length=50)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='actions', to='app.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.player')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.team')),
            ],
        ),
    ]
