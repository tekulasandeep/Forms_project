from django.shortcuts import render
from django.db import models
from detail.models import UserDetails
from django.shortcuts import redirect
# from django.template import loader
# from django.http import HttpResponse
# from django.forms import modelformset_factory



from .forms import UserModelForm

def userdetails(request):
    form = UserModelForm()  
    if request.method == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect('/')
        else:
            print(form.errors)
            return render(request,'userdetails.html',{'form': form, 'erros': form.errors})   

    else:
        return render(request,'userdetails.html',{'form': form})    
            
    
    
def user_list(request):
    users = UserDetails.objects.all()
    return render(request,  'display.html', {'users': users})








