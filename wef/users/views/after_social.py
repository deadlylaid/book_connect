from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


# Social Join us 후 redirect
class AfterSocial(View):

    def get(self, request):
        if request.user.nickname:
            return redirect(reverse("home"))
        return render(
                request,
                'users/aftersocial.html',
                context={}
                )

    def post(self, request, *args, **kwargs):

        received_User = request.user

        received_nickname = request.POST.get("nickname")
        received_phone = request.POST.get("phonenumber")

        received_User.nickname = received_nickname
        received_User.phone = received_phone
        received_User.save()

        return redirect(reverse("home"))
