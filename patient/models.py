from django.db import models
# import uuid

# STATUS_CHOICES = (
#     ('Fortis','Fortis'),
#     ('Tata','Tata'),
#     ('Manipal','Manipal'),
#     ('Govt','Govt')
#  )
class bedsinfo(models.Model):
    hospital_name = models.CharField(max_length=50)
    TotalBeds = models.IntegerField(default=0)
    CovidBeds = models.IntegerField(default=0)
    RegularBeds = models.IntegerField(default=0)

    def __str__(self):
        return self.hospital_name + ' Hospital'


# Create your models here.
class patientinfo(models.Model):
    # hospital_name = models.CharField(max_length=100)
    # patient_id = models.IntegerField(default=0, blank=True, null=True)
    patient_name = models.CharField(max_length=100)
    disease = models.CharField(max_length=100)
    medication = models.CharField(max_length=200, default = "none")
    doctor_name = models.CharField(max_length=100)
    admitted = models.BooleanField()
    
    # hospital_name = models.ForeignKey(bedsinfo, db_column="hospital_name", on_delete=models.CASCADE)
    hospital_name = models.ForeignKey(bedsinfo, on_delete=models.CASCADE)
    # 

#Name by whichm the column in list will be formed
    def __str__(self):
        return self.patient_name

# class medicinehistory(models.Model):
#     patient_id = models.IntegerField()
#     patient_name = models.CharField(max_length=100)
#     Medicines = models.CharField(max_length=500)
#     Prescription_date = models.DateField()
    
#     def __str__(self):
#         return self.patient_name + '-' + self.Prescription_date  





