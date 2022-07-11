from django.shortcuts import render, redirect 
from .models import Record, Genre, Review, User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .forms import AirPlayForm, ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



def about(request):
   return render(request, 'about.html')


def home(request):
    records = Record.objects.all()
    return render(request, 
                  'home.html', 
                  {'records': records})

@login_required 
def records_index(request):
    records = Record.objects.filter(user=request.user)
    return render(request, 
                  'records/index.html', 
                  {'records': records})

def new_record(request): 
  return render(request, 'records/new_record_form.html')

class RecordCreate(LoginRequiredMixin,CreateView):
  model = Record
  fields = ['title', 'artist', 'label', 'year', 'description']
  success_url = '/records/'
  def form_valid(self, form):
    # form.istance represents the cat
    #form.instance.user represents the user col of the cat
    #self.request.user is the currently logged-in user
    form.instance.user = self.request.user 
    return super().form_valid(form)

class RecordDelete(DeleteView):
  model = Record
  success_url = '/records/'
  fields = '__all__'

class RecordUpdate(UpdateView):
  model = Record
  success_url = '/records/'
  fields = ['title', 'artist', 'label', 'year', 'description']
    

def records_detail(request, record_id):
  record = Record.objects.get(id=record_id)
  reviews = Review.objects.filter(record=record_id)
  genres = Genre.objects.all()
  airplay_form= AirPlayForm()
  review_form = ReviewForm()
  if record.user.id == request.user.id: 
    return render(request, 'records/detail.html', { 
    'record': record, 'airplay_form': airplay_form, 'review_form': review_form, 'genres': genres, 'reviews': reviews
})
  else: 
    return render(request, 'records/public-detail.html', { 
    'record': record, 'review_form': review_form, 'genres': genres, 'reviews': reviews
})




# add_airplay
@login_required
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


@login_required
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



@login_required
def add_review(request, record_id):

   Review.objects.create(
    review = request.POST['review'],
    record = Record.objects.get(id = record_id),
    user = User.objects.get(id = request.user.id)
  )

   return redirect('detail', record_id=record_id)


# @login_required
# def comments_create(request, post_id):

#   Comments.objects.create(
#     content = request.POST['content'],
#     post = Postcreated.objects.get(id = post_id),
#     user = User.objects.get(id = request.user.id)
#   )

#   return redirect(f'/posts/{post_id}/')


# @login_required
# def comments_delete(request, comment_id, post_id):
#   post = Postcreated.objects.get(id = post_id),
#   Comments.objects.get(id=comment_id).delete()
#   return redirect(f'/posts/{post_id}/')







  
  
  
  
 

