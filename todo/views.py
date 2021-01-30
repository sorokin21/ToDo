from django.shortcuts import render
from .models import To_do_list

# Create your views here.
def home(request):
     to_do_lists = To_do_list.objects.all()
     context = {
          'to_do_lists' : to_do_lists,
     }

     return render(request,'todo/home.html', context)