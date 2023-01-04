from django.shortcuts import render
from django.http import HttpResponse,Http404

from .models import Pet
# Create your views here.
def home(request):
    #return HttpResponse('<p>Home page</p>')
    pets = Pet.objects.all()
    return render(request,'home.html',{
        'pets':pets
    })

def pet_details(request,pet_id):
   # return HttpResponse(f'<p>pet_details view with id {pet_id}</p>')
   try:
        pet = Pet.objects.get(id = pet_id)
   except Pet.DoesNotExist:
        raise Http404('pet not Found')
   return render(request , 'pet_detail.html',{
    'pet':pet,
   })