from django.shortcuts import render
from home.models import Intro, Testi, Works, Services
from django.http import HttpResponse 
from django.core.mail import send_mail

def home(request):
    intros = Intro.objects.all()
    testis = Testi.objects.all()
    workss = Works.objects.all()
    servis = Services.objects.all()
    return render(request,'index.html',{'intros':intros,'testis':testis,'workss':workss,'servis':servis})


def kontak(request):
    #check for POST requests on load.
    request.method == 'POST'
    nomor = request.POST.get('nomor')
    pesan = request.POST.get('pesan')
    email = request.POST.get('email')

    if nomor and pesan and email:
        try:
            send_mail(nomor, pesan, email, ['rezkysy@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.') 
        return render(request, 'selamat.html') 

    else:
        #loading contacts.html if no requests
        return render(request, 'kontak.html')

def selamat(request):
   return render(request, 'selamat.html') 