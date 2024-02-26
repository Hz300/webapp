# Generated by Django 5.0.2 on 2024-02-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SMRTPROPERTIES',
            fields=[
                ('imb_ID', models.AutoField(db_column='IMBID', primary_key=True, serialize=False)),
                ('imb_Category', models.CharField(db_column='IMBCATEGORY', max_length=60, null=True)),
                ('imb_Name', models.CharField(db_column='IMBNAME', max_length=120, null=True)),
                ('imb_MLS', models.FloatField(db_column='IMBMLS', null=True)),
                ('imb_Type', models.CharField(db_column='IMBTYPE', max_length=50, null=True)),
                ('imb_City', models.CharField(db_column='IMBCITY', max_length=50, null=True)),
                ('imb_State', models.CharField(db_column='IMBSTATE', max_length=50, null=True)),
                ('imb_Area', models.CharField(db_column='IMBAREA', max_length=80, null=True)),
                ('imb_Bedrooms', models.SmallIntegerField(db_column='IMBBEDROOMS', null=True)),
                ('imb_Bathrooms', models.SmallIntegerField(db_column='IMBBATHROOMS', null=True)),
                ('imb_Size', models.FloatField(db_column='IMBSIZE', null=True)),
                ('imb_Price', models.DecimalField(db_column='IMBPRICE', decimal_places=2, max_digits=12, null=True)),
                ('imb_Currency', models.CharField(db_column='CURRENCY', max_length=30, null=True)),
                ('imb_New_Flag', models.BooleanField(db_column='IMBNEWFLAG', null=True)),
                ('imb_Owner', models.CharField(db_column='IMBOWNER', max_length=80, null=True)),
                ('imb_Agent', models.CharField(db_column='IMBAGENT', max_length=80, null=True)),
                ('imb_Prom_Disc', models.BooleanField(db_column='IMBPROMDISC', null=True)),
                ('imb_Description', models.CharField(db_column='IMBDESCRIPTION', max_length=200, null=True)),
                ('imb_Active', models.BooleanField(db_column='IMBACTIVE', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SMRTWEBFORM',
            fields=[
                ('frm_id', models.AutoField(db_column='FRMID', primary_key=True, serialize=False)),
                ('frml_name', models.CharField(blank=True, db_column='FRMLNAME', max_length=60, null=True)),
                ('frm_fname', models.CharField(blank=True, db_column='FRMFNAME', max_length=60, null=True)),
                ('frm_phone', models.CharField(blank=True, db_column='FRMPHONE', max_length=15, null=True)),
                ('frm_email', models.CharField(blank=True, db_column='FRMEMAIL', max_length=50, null=True)),
                ('frm_serv', models.CharField(blank=True, db_column='FRMSERV', max_length=60, null=True)),
                ('frm_messag', models.CharField(blank=True, db_column='FRMMESSAG', max_length=80, null=True)),
                ('frm_fcont', models.BooleanField(blank=True, db_column='FRMFCONT', null=True)),
                ('frm_date', models.DateTimeField(blank=True, db_column='FRMDATE', null=True)),
            ],
            options={
                'db_table': 'SMRTWEBFORM',
                'managed': True,
            },
        ),
    ]
