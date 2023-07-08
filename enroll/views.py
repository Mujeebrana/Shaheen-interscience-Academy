from django.shortcuts import render
from .forms import StudentsRegistration
from .models import User    
# Create your views here.
def add_show(request):
    if request.method == 'POST':
     fm = StudentsRegistration(request.POST)
     if fm.is_valid():
      nm = fm.cleaned_data['name']
      em = fm.cleaned_data['email']
      pw = fm.cleaned_data['password']
      reg = User(name=nm, email=em, password=pw)
      reg.save()
     else:
         return render(request, 'enroll/addandshow.html',{'form':fm})
      
    else:
      fm = StudentsRegistration()
      
    return render(request, 'enroll/addandshow.html',{'form':fm})
