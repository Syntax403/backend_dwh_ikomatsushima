from django.contrib import admin
from .models import News
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    search_fields = ('titulo', 'autor__username')
    list_filter = ('fecha_publicacion',)

admin.site.register(News, NewsAdmin)