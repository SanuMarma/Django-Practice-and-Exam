from django.shortcuts import render
import datetime

def home(request):
    d = {'author' : 'Rahim', 'age' : 20, 'lst' : ['Python','is','best'], 'birthday' : datetime.datetime.now(), 'val' : ' ' ,'courses' : [
        {
            'id' : 1,
            'name' : 'Python',
            'fee' : 5000
        }, 

        {
            'id' : 2,
            'name' : 'Django',
            'fee' : 10000
        },
        {
            'id' : 3,
            'name' : 'C',
            'fee' : 1000
        },
    ]}
    return render(request, 'home.html', d)