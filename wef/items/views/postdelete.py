from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.contrib import messages

from items.models import ItemPost, BookList


class PostDelete(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, pk, *args, **kwargs):

        itempost = ItemPost.objects.get(pk=pk)

        # 현재 유저가 삭제하려는 포스트의 업로더와
        # 같은 유저인 것을 확인 한 후 삭제
        if request.user.username == itempost.user.username:
            itempost.is_deleted = True
            itempost.save()

            messages.add_message(
                    request,
                    messages.WARNING,
                    "정상적으로 삭제되었습니다.",
                    )
            return redirect(reverse("postlist"))

        # 같은 유저가 아니면 삭제하지 않고 리다이렉트
        else:

            messages.add_message(
                    request,
                    messages.WARNING,
                    "이런 장난은 하지 마십시오",
                    )

            return redirect(
                    reverse(
                        "postdetail",
                        kwargs={
                            'pk': itempost.id,
                            },
                        )
                    )
