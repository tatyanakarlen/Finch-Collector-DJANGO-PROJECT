from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

SEGMENTS = (
    ('B', 'Beginning'), 
    ('M', 'Middle'), 
    ('E', 'End')
)

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=50)


    def __str__(self):
        return self.genre

    def get_absolute_url(self):
        return reverse('genres_detail', kwargs={'pk': self.id})

  #------------------------------------------------------------------      


class Record(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(max_length=250)
    genres = models.ManyToManyField(Genre) #creates join table 
    user = models.ForeignKey(User, on_delete=models.CASCADE) #1 user has many posts
   
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'record_id': self.id})

    def played_today(self):
        return self.airplay_set.count() >= 1


class Review(models.Model):
  review = models.TextField(max_length=1000)
  record = models.ForeignKey(Record, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.title
   



        # return self.airplay_set.filter(date=date.today()).count() >= 1

#----------------------------------------------------    

class AirPlay(models.Model):
    date = models.DateField('Add airplay date')
    segment = models.CharField(
        max_length=1, 
        choices=SEGMENTS, 
        default=SEGMENTS[0][0]
    )

    record = models.ForeignKey(Record, on_delete=models.CASCADE)

    

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_segment_display()} on {self.date}"

 # change the default sort
    class Meta:
      ordering = ['-date']


#---------------------------------------------------------------------------------------------







