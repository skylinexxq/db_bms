from django.contrib import admin
from . import models

class ReaderInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'phone', 'email')
    search_fields = ('username', 'phone', 'email')


class LibrarianInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'phone', 'email')
    search_fields = ('username', 'phone', 'email')

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publisher', 'isbn', 'date', 'number', 'operator')
    search_fields = ('id', 'title', 'author', 'publisher', 'isbn', 'date')
    list_filter = ('operator',)

class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn_id', 'position', 'state', 'operator')
    search_fields = ('id', 'isbn_id', 'position')
    list_filter = ('position',)


admin.site.register(models.Reader)
admin.site.register(models.Librarian)
admin.site.register(models.Book)
admin.site.register(models.BookCopy)