from django.db import models

# Create your models here. Connects to a database to make queries

class Court(models.Model):
    courtname = models.CharField(max_length=30) #This attribute represents a column in the Menu table
    image = models.ImageField (upload_to = 'photo', null = True)
    courtaddress = models.CharField(max_length=300)
    numberofcourts = models.IntegerField (default = 0)
    courtofficiators = models.BooleanField(default = False)
    lights = models.BooleanField(default = False)
    closingtime = models.TimeField(null = True)

    def __str__ (self): # The underscores makes a magic method- python looks for it- it is encapsulated- enables you to return the value of the cell
        return (self.courtname)

    class Meta:
        db_table = 'Court' #Makes it so that the name is new_menu instead of travelpages_new_menu