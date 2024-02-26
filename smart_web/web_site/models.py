from django.db import models

# Create your models here.

class SMRTPROPERTIES(models.Model):
    imb_ID = models.AutoField(primary_key=True, db_column='IMBID')
    imb_Category = models.CharField(max_length=60, null=True, db_column='IMBCATEGORY')
    imb_Name = models.CharField(max_length=120, null=True, db_column='IMBNAME')
    imb_MLS = models.FloatField(null=True, db_column='IMBMLS')
    imb_Type = models.CharField(max_length=50, null=True, db_column='IMBTYPE')
    imb_City = models.CharField(max_length=50, null=True, db_column='IMBCITY')
    imb_State = models.CharField(max_length=50, null=True, db_column='IMBSTATE')
    imb_Area = models.CharField(max_length=80, null=True, db_column='IMBAREA')
    imb_Bedrooms = models.SmallIntegerField(null=True, db_column='IMBBEDROOMS')
    imb_Bathrooms = models.SmallIntegerField(null=True, db_column='IMBBATHROOMS')
    imb_Size = models.FloatField(null=True, db_column='IMBSIZE')
    imb_Price = models.DecimalField(max_digits=12, decimal_places=2, null=True, db_column='IMBPRICE')
    imb_Currency = models.CharField(max_length=30, null=True, db_column='CURRENCY')
    imb_New_Flag = models.BooleanField(null=True, db_column='IMBNEWFLAG')
    imb_Owner = models.CharField(max_length=80, null=True, db_column='IMBOWNER')
    imb_Agent = models.CharField(max_length=80, null=True, db_column='IMBAGENT')
    imb_Prom_Disc = models.BooleanField(null=True, db_column='IMBPROMDISC')
    imb_Description = models.CharField(max_length=200, null=True, db_column='IMBDESCRIPTION')
    imb_Active = models.BooleanField(null=True, db_column='IMBACTIVE')
    
    class meta:
        managed = True
        db_table = 'SMRTPROPERTIES'


class SMRTWEBFORM(models.Model):
    frm_id = models.AutoField(primary_key=True, db_column='FRMID')
    frml_name = models.CharField(max_length=60, blank=True, null=True, db_column='FRMLNAME')
    frm_fname = models.CharField(max_length=60, blank=True, null=True, db_column='FRMFNAME')
    frm_phone = models.CharField(max_length=15, blank=True, null=True, db_column='FRMPHONE')
    frm_email = models.CharField(max_length=50, blank=True, null=True, db_column='FRMEMAIL')
    frm_serv = models.CharField(max_length=60, blank=True, null=True, db_column='FRMSERV')
    frm_messag = models.CharField(max_length=80, blank=True, null=True, db_column='FRMMESSAG')
    frm_fcont = models.BooleanField(blank=True, null=True, db_column='FRMFCONT')
    frm_date = models.DateTimeField(blank=True, null=True, db_column='FRMDATE')

    class Meta:
        managed = True
        db_table = 'SMRTWEBFORM'