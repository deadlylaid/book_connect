from django.views.generic import View
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse

from django.contrib import messages

from users.models import User
from items.models import ItemPost, BookList


class MyPage(View):

    def get(self, request):

        user = request.user

        posted_Item = ItemPost.objects.filter(user=user)

        context = {
                'posts': posted_Item,
                }

        return render(
                request,
                "users/mypage.html",
                context,
                )
