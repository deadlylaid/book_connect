from django.views.generic import View
from django.shortcuts import render


class IntroduceView(View):

    def get(self, request):

        return render(
                request,
                "items/introduce.html",
                context={}
                )
