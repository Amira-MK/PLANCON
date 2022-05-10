from django.contrib import admin
from .models import Chairman, Conference, Author, Article, Reviewer

# Register your models here.

admin.site.register(Conference)
admin.site.register(Chairman)
admin.site.register(Article)
admin.site.register(Author)
admin.site.register(Reviewer)