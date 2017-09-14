from django.core.urlresolvers import resolve
from django.test import TestCase

from items.models.item_post import ItemPost

from wef.views import Home
from items.views.booksale import BookSale

from wef.mixins.tests import SetUpLogInMixin


class BookSalePageTest(SetUpLogInMixin):

    def test_booksale_url_resolves_to_home_view(self):
        found = resolve('/booksale/')
        self.assertEqual(found.func.__name__, BookSale.__name__)

    def test_booksale_page_template(self):
        response = self.client.get('/booksale/')
        self.assertTemplateUsed(response, 'items/booksale.html')


class NewBookSaleTest(SetUpLogInMixin):

    def test_client_post_books(self):

        send_post_data_post = self.client.post(
                '/booksale/',
                data={
                    'title': '책 팝니다',
                    'book': ['book1', 'book2'],
                    'price': ['1000', '2000'],
                    }
                )

        new_post = ItemPost.objects.first()
        self.assertEqual(new_post.title, '책 팝니다')

        send_post_price_is_null_data = self.client.post(
                '/booksale/',
                data={
                    'title': '책팜2',
                    'book': ['book1', 'book2'],
                    'price': ['가격미정', '2000'],
                    'is_price_null': ['True', 'True'],
                    }
                )

        second_post = ItemPost.objects.last()
        self.assertEqual(second_post.title, '책팜2')
        self.assertEqual(second_post.booklist_set.first().bookprice, 0)
