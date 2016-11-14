from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.contrib import messages

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

        # 등록된 책이 한권도 없을 때
        if not book_names:
            messages.add_message(
                    request,
                    messages.WARNING,
                    "최소한 한권 이상의 도서가 등록되어야 합니다."
                    )

            return redirect(reverse('booksale'))

        else:
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
