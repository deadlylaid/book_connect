from django.apps import AppConfig
from watson import search as watson


class ItemsAppConfig(AppConfig):

    name = "items"

    def ready(self):
        ItemModel = self.get_model("ItemPost")
        watson.register(ItemModel, fields=["title", "booklist_set__bookname", ])
