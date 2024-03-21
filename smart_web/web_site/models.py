from django.db import models
from django.utils import timezone
import os

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
    imb_Description_Es = models.CharField(max_length=200, null=True, db_column='IMBDESCRIPTIONES')
    imb_Active = models.BooleanField(null=True, db_column='IMBACTIVE')
    imb_Creation_Time = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f"{self.imb_ID} {self.imb_Name}"

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.imb_Creation_Time = timezone.now()
        super().save(*args, **kwargs)

    class Meta:
        managed = True
        db_table = 'SMRTPROPERTIES'

def get_image_path(instance, filename):
        # Generate the folder path based on the property ID
        property_id = instance.property.imb_ID
        return f'property_images/{property_id}/{filename}'

class PropertyImage(models.Model):
    property = models.ForeignKey(SMRTPROPERTIES, on_delete=models.CASCADE, )  # Forward reference to SMRTPROPERTIES
    image = models.ImageField(upload_to=get_image_path, null=True, blank=True, db_column='IMAGES')

    class Meta:
        managed = True
        db_table = 'PROPERTYIMAGES'  # 


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
        

def get_asociate_path(instance, filename):
    """
    Generates a unique path for the uploaded image based on associate name.
    """
    associate_name = instance.nombre.lower().replace(" ", "_")  # Sanitize name
    return os.path.join('asociates', associate_name, filename)

class Asociados(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    area_expertis = models.CharField(max_length=255)
    puesto = models.CharField(max_length=255)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to=get_asociate_path, blank=True)  # Allow blank images
    activo = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.nombre} ({self.area_expertis})"

    class Meta:
        managed = True