from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'djangofier/home.html',{"activeLi":"home"})

def about(request):
    return render(request,'djangofier/about.html',{"activeLi":"about"})

def menu(request):
    return render(request,'djangofier/menu.html',{"activeLi":"menu"})

def events(request):
    return render(request,'djangofier/events.html',{"activeLi":"events"})

def specials(request):
    return render(request,'djangofier/specials.html',{"activeLi":"specials"})

def gallery(request):
    return render(request,'djangofier/gallery.html',{"activeLi":"gallery"})

def chefs(request):
    return render(request,'djangofier/chefs.html',{"activeLi":"chefs"})

def chef1(request):
    return render(request,'djangofier/chef1.html',{"activeLi":"chefs"})

def chef2(request):
    return render(request,'djangofier/chef2.html',{"activeLi":"chefs"})

def chef3(request):
    return render(request,'djangofier/chef3.html',{"activeLi":"chefs"})

def contact(request):
    return render(request,'djangofier/contact.html',{"activeLi":"contact"})

def book(request):
    return render(request, 'djangofier/bookatable.html')