from django.views.generic import View
from watson import search as watson
from django.http import HttpResponse


class SearchView(View):

    def get(self, request):
        return HttpResponse("hello world")
