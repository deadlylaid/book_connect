from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from items.models import BookList, ItemPost


class PostDetail(View):

    def get(self, request, pk):

        post = ItemPost.objects.get(pk=pk)

        books = post.booklist_set.order_by('booknumber')
        images = post.bookimage_set.all()

        context = {
                "post": post,
                "books": books,
                "images": images,
                }

        return render(
               request,
               'items/detail.html',
               context,
               )
