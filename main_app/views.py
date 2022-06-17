from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .models import Record, Genre
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import AirPlayForm



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
    return render(request, 'home.html')

   

# def seed(request):
#     #create few records 
#     Record.objects.create(title='Parallel Lines', 
#                           artist= 'Blondie', 
#                           label= 'Chrysalis', 
#                           year= '1978', 
#                           description = "Blondie's most polished and commercial sound to date"
#                             )
#     Record.objects.create(title='The Well-Tempered Clavier Book I & II: J.S.Bach', 
#                           artist= 'Svyatoslav Richter', 
#                           label= 'Melodiya', 
#                           year= '1971', 
#                           description = "Legendary recording of one of Bach's greatest works by renowed Russian pianist"
#                             )
#     Record.objects.create(title='Love To Love You Baby', 
#                           artist= 'Donna Summer', 
#                           label= 'Casablanca', 
#                           year= '1975', 
#                           description = "Sleazy disco classic, on heavy rotation at Studio 54"
#                             )
#     Record.objects.create(title='Rebel Yell', 
#                           artist= 'Billy Idol', 
#                           label= 'Chrysalis', 
#                           year= '1983', 
#                           description = "London punk Billy Idol is back with a rock/new-wave album"
#                             )
#     Record.objects.create(title='Madonna', 
#                           artist= 'Madonna', 
#                           label= 'SIRE', 
#                           year= '1983', 
#                           description = "New artist Madonna blows everyone away with fresh club/pop sound"
#                             )
#     return HttpResponse('done')


def records_index(request):
    records = Record.objects.all()
    print('records from database', records)
    return render(request, 
                  'records/index.html', 
                  {'records': records})
    
# def show(request, record_id):
#         print('incoming wildcard value is' , record_id)
#         #hey database, please get me the record with id=2
#         record = Record.objects.get(id=record_id)
#         return render(request, 'records/detail.html', {'record': record})

def records_detail(request, record_id):
  record = Record.objects.get(id=record_id)
  airplay_form= AirPlayForm()
  return render(request, 'records/detail.html', { 
    'record': record, 'airplay_form': airplay_form,
})


def new_record(request): 
  return render(request, 'records/new_record_form.html')

class RecordCreate(CreateView):
  model = Record
  fields = '__all__'
  success_url = '/records/'

class RecordDelete(DeleteView):
  model = Record
  success_url = '/records/'
  fields = '__all__'

class RecordUpdate(UpdateView):
  model = Record
  success_url = '/records/'
  fields = '__all__'

# add_airplay

def add_airplay(request, record_id):
  #create the ModelForm using the data in request.POST
  form = AirPlayForm(request.POST)
  #validate the form
  if form.is_valid():
    #don't save form to db until it has the cat_id assigned 
    new_airplay = form.save(commit=False)
    new_airplay.record_id = record_id 
    new_airplay.save()
  return redirect('detail', record_id=record_id)


# def add_feeding(request, cat_id):
# 	# create the ModelForm using the data in request.POST
#   form = FeedingForm(request.POST)
#   # validate the form
#   if form.is_valid():
#     # don't save the form to the db until it
#     # has the cat_id assigned
#     new_feeding = form.save(commit=False)
#     new_feeding.cat_id = cat_id
#     new_feeding.save()
#   return redirect('detail', cat_id=cat_id)






# class CatUpdate(UpdateView):
#   model=Cat
#   fields = ['name','breed', 'description', 'age']
#   success_url='/cats/'

# class CatDelete(DeleteView):
#   model = Cat
#   success_url = '/cats/'
#   fields = ['breed', 'description', 'age']

#long manual way of creating:

# def create_standard(request):
#   try:
#     print('incoming form data', request.POST)
#     name = request.POST['name']
#     breed = request.POST['breed']
#     description = request.POST['description']
#     age = request.POST['age']
    
#     Cat.objects.create(name= name, 
#                        breed = breed, 
#                        description = description,
#                        age = age)

#     return redirect('/cats')
#   except:
#      return HttpResponse('something went wrong')
  
  
  
  
 

