from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from items.models import ItemPost


class PostList(View):

    def get(self, request):

        page = request.GET.get("page", 1)
        page_per = request.GET.get("per", 5)

        paginator = Paginator(
                # 가장 나중에 만들어진 포스트를 먼저 꺼내기 위해 '-id'사용
                ItemPost.objects.filter(is_deleted=False).order_by('-id'),
                page_per,
                )

        posts = paginator.page(page)

        # 페이지 리스트 커스터마이징
        page_list = []
        for page_number in posts.paginator.page_range:
            if page_number == 1 or (page_number-2) <= posts.number <= (page_number+2) \
                    or page_number == posts.paginator.count:
                page_list.append(page_number)
                print(page_list)
            else:
                if page_list[-1] == '...':
                    print(page_list)
                    continue
                else:
                    page_list.append('...')
                    print(page_list)

        context = {
                "posts": posts,
                "page_list": page_list,
                }
        return render(
               request,
               'items/list.html',
               context,
               )
