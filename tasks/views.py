from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1>❤️welcome to Mscoial\'s❤️ website</h1>')

def about(request):
    return HttpResponse('<h1><p>Msocials is a social media management and growth platform that helps individuals and businesses manage, schedule, and boost their presence across all major social media platforms — including Instagram, Facebook, Twitter/X, TikTok, and more. From content scheduling to engagement tracking and audience growth, Msocials makes it easy to build a stronger, more consistent online presence in one place.\'s website</h1></p>')

def contact(request):
    return HttpResponse('<h1><p>Email:ozurumbachinecherem28@gmail.com\'s website</h1></p>')