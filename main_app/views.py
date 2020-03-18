from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Puppy, Toy
from .forms import FeedingForm

class PuppyCreate(CreateView):
  model = Puppy
  fields = ['name', 'breed', 'description', 'age']

class PuppyUpdate(UpdateView):
  model = Puppy
  fields = ['breed', 'description', 'age']

class PuppyDelete(DeleteView):
  model = Puppy
  success_url = '/puppies/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def puppies_index(request):
  puppies = Puppy.objects.all()
  return render(request, 'puppies/index.html', { 'puppies': puppies })

def puppies_detail(request, puppy_id):
  puppy = Puppy.objects.get(id=puppy_id)
  toys_puppy_doesnt_have = Toy.objects.exclude(id__in = puppy.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'puppies/detail.html', {
    'puppy': puppy, 'feeding_form': feeding_form,
    'toys': toys_puppy_doesnt_have
  })

def add_feeding(request, puppy_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.puppy_id = puppy_id
    new_feeding.save()
  return redirect('detail', puppy_id=puppy_id)

def assoc_toy(request, puppy_id, toy_id):
  Puppy.objects.get(id=puppy_id).toys.add(toy_id)
  return redirect('detail', puppy_id=puppy_id)

def unassoc_toy(request, puppy_id, toy_id):
  Puppy.objects.get(id=puppy_id).toys.remove(toy_id)
  return redirect('detail', puppy_id=puppy_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'