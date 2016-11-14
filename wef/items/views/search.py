from django.views.generic import View
from django.shortcuts import render
from items.models import ItemPost


class SearchView(View):

    def get(self, request):

        keyword = request.GET.get("keyword")

        if keyword:
            search_result = ItemPost.objects.filter(
                    title=keyword,
                    )

            if search_result:
                context = {
                        "posts": search_result,
                        }
            else:
                context = {
                        "posts": False,
                        "keyword": keyword,
                        }

        return render(
                request,
                'items/list.html',
                context,
                )
