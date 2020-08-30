from django.contrib import admin
from .models import Post,Type, Category
# from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Post)
admin.site.register(Type)
admin.site.register(Category)

# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)