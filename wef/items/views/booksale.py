from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse

from items.models import ItemPost, BookList


class BookSale(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request):

        if request.user.phone:

            return render(
                   request,
                   'items/booksale.html',
                   context={}
                   )

        return render(
                request,
                'users/aftersocial.html',
                context={}
                )

    def post(self, request):

        title = request.POST.get('title')
        book_names = request.POST.getlist('book')
        book_prices = request.POST.getlist('price')

        saler = request.user

        created_bookpost = ItemPost.objects.create(
                user=saler,
                title=title,
                )

        for i, names in enumerate(book_names):
            BookList.objects.create(
                    post=created_bookpost,
                    booknumber=i+1,
                    bookname=names,
                    bookprice=book_prices[i],
                    )

        return redirect(
                reverse(
                    "postdetail",
                    kwargs={
                        'pk': created_bookpost.id,
                        }
                    )
                )
