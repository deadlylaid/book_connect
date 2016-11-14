from django.contrib import admin

from items.models import *


# ItemPost admin에 BookList를 노출시키기위한 코드
class BookListTabularAdmin(admin.TabularInline):
    model = BookList
    readonly_fields = ('booknumber',)
    can_delete = False


@admin.register(ItemPost)
class ItemModelAdmin(admin.ModelAdmin):

    list_display = admin.ModelAdmin.list_display + (
            'user',
            'user_nickname',
            'title',
            'created_at',
            'updated_at',
            )

    search_fields = (
            'title',
            )

    readonly_fields = (
            'user_nickname',
            'created_at',
            'updated_at',
            )

    inlines = [
            BookListTabularAdmin,
            ]
