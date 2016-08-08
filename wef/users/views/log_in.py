from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate


class LogInView(View):

    def get(self, request):
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
