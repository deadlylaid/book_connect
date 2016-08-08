from django.views.generic import View
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout


class LogOutView(View):

    def get(self, request, *args, **kwags):
        logout(request)
        return redirect(
                reverse(
                    "home",
                    )
                )
