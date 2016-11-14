from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from items.models import ItemPost


class Home(View):

    def get(self, request):

        page = 1
        page_per = 5

        paginator = Paginator(
                ItemPost.objects.filter(is_deleted=False).order_by('-id'),
                page_per,
                )

        posts = paginator.page(page)

        context = {
                "posts": posts
                }

        return render(
                request,
                'home.html',
                context,
                )
