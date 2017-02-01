from django.views.generic import View
from django.shortcuts import render
from items.models import ItemPost
from django.core.paginator import InvalidPage, Paginator

from haystack.views import SearchView

"""
django-haystack code
link - https://github.com/django-haystack/django-haystack/blob/master/haystack/views.py
"""


class SearchView(SearchView):

    def build_page(self):

        """
        Paginates the results appropriately.
        In case someone does not want to use Django's built-in pagination, it
        should be a simple matter to override this method to do what they would
        like.
        """
        try:
            page_no = int(self.request.GET.get('page', 1))
        except (TypeError, ValueError):
            raise Http404("Not a valid number for page.")

        if page_no < 1:
            raise Http404("Pages should be 1 or greater.")

        start_offset = (page_no - 1) * self.results_per_page
        self.results[start_offset:start_offset + self.results_per_page]

        # page per 5 posts
        paginator = Paginator(self.results, 5)

        try:
            page = paginator.page(page_no)
        except InvalidPage:
            raise Http404("No such page!")

        return (paginator, page)

    def create_response(self):

        (paginator, page) = self.build_page()

        context = {
            'query': self.query,
            'form': self.form,
            'page': page,
            'results': self.results,
            'paginator': paginator,
            'suggestion': None,
        }

        return render(self.request, self.template, context)
        """
        Generates the actual HttpResponse to send back to the user.
        """
