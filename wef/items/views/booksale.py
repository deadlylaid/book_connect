from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.contrib import messages

from items.models import ItemPost, BookList, BookImage
from items.tasks.haystack_indexing import UpdateIndexTask


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
        images = request.FILES.getlist('images')

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
                if book_prices[i] == '가격미정':
                    book_prices[i] = 0
                BookList.objects.create(
                        post=created_bookpost,
                        booknumber=i+1,
                        bookname=names,
                        bookprice=book_prices[i],
                        )

            # 한 포스트당 이미지는 3개 까지만 등록가능
            for i, image in enumerate(images[:3]):
                BookImage.objects.create(
                        post=created_bookpost,
                        image=image,
                        )

            # django-haystack auto indexing
            auto_indexing = UpdateIndexTask()
            auto_indexing.delay()

            return redirect(
                    reverse(
                        "postdetail",
                        kwargs={
                            'pk': created_bookpost.id,
                            }
                        )
                    )
