from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.contrib import messages

from users.models import User
from items.models import ItemPost


class PassWordReSet(TemplateView):

    template_name = 'users/passwordreset.html'
    model = User
    fields = [
            'password',
            ]

    def post(self, request):

        searched_user = request.POST.get('hidden_username')
        new_password = request.POST.get('password-check')
        user = User.objects.get(username=searched_user)

        user.set_password(new_password)
        user.save()

        messages.add_message(
                request,
                messages.WARNING,
                "비밀번호가 정상적으로 변경되었습니다.",
                )

        return redirect(reverse('home'))
