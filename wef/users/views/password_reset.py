from django.views.generic import TemplateView, CreateView, UpdateView

from users.models import User
from items.models import ItemPost


class PassWordReSet(TemplateView):

    template_name = 'users/passwordreset.html'
