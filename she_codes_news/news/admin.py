from django.contrib import admin
from news.models import NewsStory, Category


admin.site.register(NewsStory)
admin.site.register(Category)

# Register your models here.
