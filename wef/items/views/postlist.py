from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from items.models import ItemPost


class PostList(View):

    def get(self, request):

        page = request.GET.get("page", 1)
        page_per = request.GET.get("per", 1)

        paginator = Paginator(
                ItemPost.objects.all(),
                page_per,
                )

        posts = paginator.page(page)

        context = {
                "posts": posts,
                }
        return render(
               request,
               'items/list.html',
               context,
               )
