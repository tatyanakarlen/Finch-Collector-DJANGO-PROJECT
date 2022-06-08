from django.http import HttpResponse 
from django.shortcuts import render
from .models import Record




# Create your views here.

# def index(request):
#     return render(request, 'records/index.html', { "records": records })

def about(request):
     #assumes about.html is in templates
    #hey database, it seems the user has accessed the product id 5 
    #please give me the data for product id 
    return render(request, 'about.html')
    # return HttpResponse('<h1>About the record collector</h1>')


#define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>') #django equiv of res.send 

   

def seed(request):
    #create few records 
    Record.objects.create(title='Parallel Lines', 
                          artist= 'Blondie', 
                          label= 'Chrysalis', 
                          year= '1978', 
                          description = "Blondie's most polished and commercial sound to date"
                            )
    Record.objects.create(title='The Well-Tempered Clavier Book I & II: J.S.Bach', 
                          artist= 'Svyatoslav Richter', 
                          label= 'Melodiya', 
                          year= '1971', 
                          description = "Legendary recording of one of Bach's greatest works by renowed Russian pianist"
                            )
    Record.objects.create(title='Love To Love You Baby', 
                          artist= 'Donna Summer', 
                          label= 'Casablanca', 
                          year= '1975', 
                          description = "Sleazy disco classic, on heavy rotation at Studio 54"
                            )
    Record.objects.create(title='Rebel Yell', 
                          artist= 'Billy Idol', 
                          label= 'Chrysalis', 
                          year= '1983', 
                          description = "London punk Billy Idol is back with a rock/new-wave album"
                            )
    Record.objects.create(title='Madonna', 
                          artist= 'Madonna', 
                          label= 'SIRE', 
                          year= '1983', 
                          description = "New artist Madonna blows everyone away with fresh club/pop sound"
                            )
    return HttpResponse('done')


def records_index(request):
    records = Record.objects.all()
    print('records from database', records)
    return render(request, 
                  'records/index.html', 
                  {'records': records})
    
def show(request, record_id):
        print('incoming wildcard value is' , record_id)
        #hey database, please get me the record with id=2
        record = Record.objects.get(id=record_id)
        return render(request, 'records/detail.html', {'record': record})


