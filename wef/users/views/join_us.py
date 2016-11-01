from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages

from users.models import User


def join_us(request):
    
    # GET method 로 받았을 때
    if request.method == "GET":
        return render(
                request,
                'users/joinus.html',
                context={}
                )

    # POST method 로 받았을 때
    elif request.method == "POST":
        username = request.POST.get("username")
        checkpassword = request.POST.get("checkpassword")
        password = request.POST.get("password")

        clients_already_exist = User.objects.filter(username=username)

        # POST로 받은 username이 이미 존재하는 username일 경우
        if clients_already_exist:
            messages.add_message(
                    request,
                    messages.WARNING,
                    "중복된 아이디입니다."
                    )
            return redirect(reverse(join_us))

        # 패스워드와 패스워드 확인이 일치할 경우
        elif checkpassword == password:
            created_user = User.objects.create_user(
                    username=username,
                    password=password,
                    )

            created_user = authenticate(
                    username=username,
                    password=password,
                    )

            login(request, created_user)

            return redirect(reverse("aftersocial"))

        #일치하지 않을 경우
        return redirect(reverse("join_us"))
