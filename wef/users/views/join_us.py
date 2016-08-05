from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

from users.models import User


def join_us(request):

    if request.method == "GET":
        return render(
                request,
                'users/joinus.html',
                context={}
                )

    elif request.method == "POST":
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        created_user = User.objects.create_user(
                username=username,
                password=password,
                phone=phone,
                )

        return redirect(reverse("home"))
