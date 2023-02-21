from django.shortcuts import HttpResponse, render, redirect
from .forms import Basic_Form
from .models import BasicForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = Basic_Form(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.name = form.clean_name()
            data.email = form.clean_email()
            data.phone = form.clean_phone()
            data.bday = form.clean_bday()
            data.save()
            return redirect('form.html')
    else:
        form = Basic_Form()
    return render(request, 'index.html', {'form': form})

def form_details(request):
    context = {
        'form_details' : BasicForm.objects.all()
    }
    return render(request,'form.html',context)