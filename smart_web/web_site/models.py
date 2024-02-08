from django.db import models

# Create your models here.
class SmrtProperties(models.Model):
    imb_ID = models.AutoField(primary_key=True)
    imb_Category = models.CharField(max_length=60, null=True)
    imb_Name = models.CharField(max_length=120, null=True)
    imb_MLS = models.FloatField(null=True)
    imb_Type = models.CharField(max_length=50, null=True)
    imb_City = models.CharField(max_length=50, null=True)
    imb_State = models.CharField(max_length=50, null=True)
    imb_Area = models.CharField(max_length=80, null=True)
    imb_Bedrooms = models.SmallIntegerField(null=True)
    imb_Bathrooms = models.SmallIntegerField(null=True)
    imb_Size = models.FloatField(null=True)
    imb_Price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    imb_Currency = models.CharField(max_length=30, null=True)
    imb_New_Flag = models.BooleanField(null=True)
    imb_Owner = models.CharField(max_length=80, null=True)
    imb_Agent = models.CharField(max_length=80, null=True)
    imb_Prom_Disc = models.BooleanField(null=True)
    imb_Description = models.CharField(max_length=200, null=True)
    imb_Active = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.imb_ID}: {self.imb_City} to {self.imb_Agent}"