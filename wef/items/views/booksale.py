from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin


class BookSale(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):

        return render(
               request,
               'items/booksale.html',
               context={}
               )

    def post(self, request):

        title = request.POST.get('title')
        book_names = request.POST.getlist('book')
        book_prices = request.POST.getlist('price')
