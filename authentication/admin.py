from django.contrib import admin
from .models import Chaiman, Conference, Author, Article

# Register your models here.

admin.site.register(Conference)
admin.site.register(Chaiman)
admin.site.register(Article)
admin.site.register(Author)