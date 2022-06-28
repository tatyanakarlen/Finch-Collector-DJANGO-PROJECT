from django.shortcuts import render, redirect 
from .models import Record, Genre
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .forms import AirPlayForm



def about(request):
   return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')

   
def records_index(request):
    records = Record.objects.all()
    return render(request, 
                  'records/index.html', 
                  {'records': records})

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
    

def records_detail(request, record_id):
  record = Record.objects.get(id=record_id)
  genres = Genre.objects.all()
  airplay_form= AirPlayForm()
  return render(request, 'records/detail.html', { 
    'record': record, 'airplay_form': airplay_form, 'genres': genres,
})




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

def assoc_genre(request, record_id, genre_id):
  r = Record.objects.get(id=record_id)
  r.genres.add(genre_id)
  return redirect('detail', record_id=record_id)

class GenreList(ListView):
  model = Genre

class GenreDetail(DetailView):
  model = Genre

class GenreCreate(CreateView):
  model = Genre
  fields = ['genre']

class GenreUpdate(UpdateView):
  model = Genre
  fields = ['genre']

class GenreDelete(DeleteView):
  model = Genre
  success_url = '/genres/'





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
  
  
  
  
 

