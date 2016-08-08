from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate

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

        created_user = authenticate(
                username=username,
                password=password,
                )

        login(request, created_user)

        return redirect(reverse("aftersocial"))
