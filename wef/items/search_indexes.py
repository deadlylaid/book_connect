from haystack import indexes

from items.models import BookList
import datetime


class BookListIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    # NgramField needs search asian language
    bookname = indexes.NgramField(model_attr='bookname')
    bookprice = indexes.CharField(model_attr='bookprice')

    def get_model(self):
        return BookList

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
