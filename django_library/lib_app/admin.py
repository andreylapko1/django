from django.contrib import admin
from django.contrib import admin
from .models import Author, Book, Review, Member, Category, Library

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_id', 'category_id', 'pub_date', 'library_id')
    search_fields = ('title', 'author_id__name')
    list_filter = ('genre', 'pub_date')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'reviewer', 'rating')
    search_fields = ('book__title', 'reviewer__name')
    list_filter = ('rating',)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name__surname',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name',)
# Register your models here.
