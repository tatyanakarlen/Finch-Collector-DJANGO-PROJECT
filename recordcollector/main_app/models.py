from django.db import models

# Create your models here.

class Record(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=250)

    
#tostring 'dunder' method, lets you print specifically what we see in the terminal 
# when we print out cat    
    def __str__(self):
        return self.title

# records = [
#     Record('Parallel Lines', 'Blondie', 'Chrysalis', 1978), 
#     Record('The Well-Tempered Clavier Book I & II: J.S.Bach', 'Svyatoslav Richter', 'Melodiya', 1971), 
#     Record('Love To Love You Baby', 'Donna Summer', 'Casablanca', 1975), 
#     Record('Rebel Yell', 'Billy Idol', 'Chrysalis', 1983),
#     Record('Madonna', 'Madonna', 'Sire', 1983)
# ]
