from django.views.generic import View
from django.shortcuts import render


class BookSale(View):

    def get(self, request):

        return render(
               request,
               'items/booksale.html',
               context={}
               )

    def post(self, request):
        pass
