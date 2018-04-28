from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def teamDetails(request):
    teamMembers = {
        'teamMembers': [
            {'firstName': 'Alexiuc',
            'lastName': 'Bianca',
            'role':'Front end developer'},
            {'firstName': 'Rotaru',
             'lastName': 'Ioan',
            'role':'Team Leader'},
            {'firstName': 'Furtuna',
            'lastName': 'Daniel',
            'role':'Designer/ Front end'},
            {'firstName': 'Soiman',
            'lastName': 'Andrei',
            'role':'Backend Developer'},

            {'firstName': 'Dimitrova',
            'lastName': 'Taia',
            'role':'QA engineer'}
        ]}

    return render(request, 'schedular/team-details.html', teamMembers)

