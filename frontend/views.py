from django.shortcuts import render
from django.http import HttpResponse
from .models import management


# Create your views here.
def home(request):
    return render(request, 'frontend/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'frontend/about.html', {'title': 'about'})

def team(request):
    team1 = management()
    team1.name = 'Charles Kanu Ikeah'
    team1.job_title = 'Director'
    team1.description = 'Department of Pollution Control and Environmental Health'
    team1.img = 'team-1.jpg'

    team2 = management()
    team2.name = 'Sharon Ikeazor'
    team2.job_title = 'Minister Of Environment'
    team2.description = 'Federal Ministry of Environment'
    team2.img = 'team-2.jpg'

    team3 = management()
    team3.name = 'Hassan Musa'
    team3.job_title = 'Permanent Secretary'
    team3.description = 'Federal Ministry of Environment'
    team3.img = 'team-3.jpg'
    teams = [team1, team2, team3]

    return render(request, 'frontend/team.html', {'title': 'Team', 'teams': teams})


def contact(request):
    return render(request, 'frontend/contact.html', {'title': 'Contact'})

def forms(request):
    return render(request, 'frontend/forms.html', {'title': 'forms'})

def mmis(request):
    return render(request, 'frontend/mmis.html', {'title': 'mmis'})

def testpage(request):
    return HttpResponse('Test PAGE')
