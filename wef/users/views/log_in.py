from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate
from django.contrib import messages


class LogInView(View):

    def get(self, request):
        if request.GET.get('next', ''):
            messages.add_message(
                    request,
                    messages.WARNING,
                    "로그인을 해야 이용하실 수 있는 서비스입니다."
                    )

        return render(
                request,
                'users/login.html',
                context={}
                )

    def post(self, request):

        received_id = request.POST.get("username")
        received_pw = request.POST.get("password")

        # authenticate은 기존 user 테이블에 존재하는
        # 데이터와 일치하는지 확인
        user = authenticate(
                username=received_id,
                password=received_pw,
                )
        if user:
            login(request, user)
            return redirect(
                    reverse("home")
                    )
        return redirect(
                reverse("log_in")
                )
