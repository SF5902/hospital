from django.db import models

#what data we need to get by input

class hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    beds_available = models.IntegerField()
    regular_beds = models.IntegerField(default=0)
    covid_beds = models.IntegerField(default=0)
    

#Name by whichm the column in list will be formed
    def __str__(self):
        return self.hospital_name + ' ' + str(self.covid_beds) + ' ' + str(self.regular_beds) + ' ' + str(self.beds_available)
