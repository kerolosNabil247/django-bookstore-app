from django.contrib import admin
from home.models import *
# Register your models here.

class ISBNInline(admin.StackedInline):
    model = ISBN
    max_num = 1
    # Prevent deleting the ISBN inline directly, as it's a primary key linked to the Book
    can_delete = False

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'rate', 'views', 'user', 'get_isbn_author', 'get_isbn_book_title')
    list_filter = ('title', 'rate', 'user', 'categories')
    search_fields = ('title', 'rate','description')
    inlines = [ISBNInline]

    def get_isbn_author(self, obj):
        return obj.isbn_details.author_title if hasattr(obj, 'isbn_details') else '-'
    
    def get_isbn_book_title(self, obj):
        return obj.isbn_details.book_title if hasattr(obj, 'isbn_details') else '-'

admin.site.register(Books, BookAdmin)
admin.site.register(Categories)
admin.site.register(ISBN)