from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Item

def index(request):
  items = Item.objects.all()
  return render(request, 'index.html', { 'items' : items })

class ItemCreate(CreateView):
  model = Item
  fields = '__all__'
  success_url = '/'

class ItemDelete(CreateView):
  model = Item
  fields = '__all__'
  success_url = '/'