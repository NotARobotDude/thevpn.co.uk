# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-11 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ipam', '0001_initial'),
        ('routing', '0003_auto_20161205_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouterConnection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_router', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_routers', to='routing.Router')),
                ('iprange', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipam.IPNetwork')),
                ('to_router', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_routers', to='routing.Router')),
                ('vpn_server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='routing.VPNServer')),
            ],
        ),
        migrations.AddField(
            model_name='router',
            name='peers',
            field=models.ManyToManyField(related_name='_router_peers_+', through='routing.RouterConnection', to='routing.Router'),
        ),
        migrations.AlterUniqueTogether(
            name='routerconnection',
            unique_together=set([('from_router', 'to_router')]),
        ),
    ]
