from django.shortcuts import render
from django.http import HttpResponse


def join_us(request):
    return render(
            request,
            'users/joinus.html',
            context={}
            )
